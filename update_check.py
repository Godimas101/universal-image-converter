# update_check.py — lightweight "is there a newer release?" check.
#
# Stdlib only. Fails silent: returns None on any error or when already current.
# No self-install — the app just links the user to the release page.

import json
import re
import threading
import urllib.request


def _ver_tuple(s):
    m = re.search(r"(\d+(?:\.\d+)*)", s or "")
    return tuple(int(p) for p in m.group(1).split(".")) if m else ()


def check(repo, current_version, *, timeout=6):
    """Return {'version', 'url'} if a newer GitHub release exists, else None."""
    try:
        api = "https://api.github.com/repos/%s/releases/latest" % repo
        req = urllib.request.Request(api, headers={
            "User-Agent": "%s-update-check" % repo.split("/")[-1],
            "Accept": "application/vnd.github+json",
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.load(resp)
        tag = data.get("tag_name") or ""
        if not _ver_tuple(tag) or _ver_tuple(tag) <= _ver_tuple(current_version):
            return None
        return {
            "version": tag.lstrip("v"),
            "url": data.get("html_url") or ("https://github.com/%s/releases/latest" % repo),
        }
    except Exception:
        return None


def check_async(repo, current_version, on_result, *, timeout=6):
    """Run check() on a daemon thread; call on_result(info_or_None) when done.
    on_result runs on the worker thread — marshal to the UI thread inside it."""
    def worker():
        try:
            r = check(repo, current_version, timeout=timeout)
        except Exception:
            r = None
        try:
            on_result(r)
        except Exception:
            pass
    threading.Thread(target=worker, daemon=True).start()
