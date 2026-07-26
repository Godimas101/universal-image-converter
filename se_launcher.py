#!/usr/bin/env python3
"""
se_launcher.py — SE Universal Image Converter entry point.

Run this file to launch the SE Image Converter:
  python se_launcher.py

The launcher manages a single top-level window whose content is swapped
between screens via show_screen().  Each screen is a ttk.Frame subclass
that receives (parent, app) and fills the window.
"""

import sys
import tkinter as tk
import webbrowser
from tkinter import ttk
from pathlib import Path

import se_theme as T
import update_check
import version

_HELP_URL = "https://github.com/Godimas101/universal-image-converter#readme"

# Lazy imports — screen modules are imported on first use to keep startup fast
_screen_modules: dict[str, object] = {}


def _load_screen(name: str):
    global _screen_modules
    if name not in _screen_modules:
        if name == "home":
            from screen_home import HomeScreen
            _screen_modules["home"] = HomeScreen
        elif name == "setup":
            from screen_setup import SetupScreen
            _screen_modules["setup"] = SetupScreen
        elif name == "image_converter":
            from screen_image_converter import ImageConverterScreen
            _screen_modules["image_converter"] = ImageConverterScreen
        elif name == "text_converter":
            from screen_text_converter import TextConverterScreen
            _screen_modules["text_converter"] = TextConverterScreen
    return _screen_modules[name]


# All screens share the same window size
_WINDOW_SIZE = "700x840"
_GEOMETRY: dict[str, str] = {
    "home":            _WINDOW_SIZE,
    "setup":           _WINDOW_SIZE,
    "image_converter": _WINDOW_SIZE,
    "text_converter":  _WINDOW_SIZE,
}


class SEToolsApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Universal Image Converter")
        self.configure(bg=T.BG)
        self.resizable(False, False)

        # Configure styles once for the whole application lifetime
        self._style = ttk.Style(self)
        T.configure_styles(self._style)

        # Combobox listbox colours (must be set on the root window)
        self.option_add("*TCombobox*Listbox*Background",       T.PANEL)
        self.option_add("*TCombobox*Listbox*Foreground",       T.TEXT)
        self.option_add("*TCombobox*Listbox*SelectBackground", T.BLUE)
        self.option_add("*TCombobox*Listbox*Font",             ("Courier New", 10))

        # Window icon
        self._icon = T.build_icon_photoimage(self)
        if self._icon:
            try:
                self.iconphoto(True, self._icon)
            except Exception:
                pass

        # Container that fills the whole window; screens are packed into it
        self._container = ttk.Frame(self, style="TFrame")
        self._container.pack(fill="both", expand=True)

        self._current_screen = None

        # Global help shortcut (screens add their own via T.bind_shortcuts)
        self.bind("<F1>", lambda _e: webbrowser.open(_HELP_URL))

        self.show_screen("home")

        # Update check — reveal an "Update available" link on the home screen if
        # a newer GitHub release exists. Background, non-blocking, fails silent.
        self.update_info = None
        update_check.check_async(version.REPO, version.APP_VERSION,
                                 self._on_update_result)

    # -----------------------------------------------------------------------

    def _on_update_result(self, info) -> None:
        """Called (on the check daemon thread) with the update dict or None."""
        self.update_info = info
        if info:
            try:
                self.after(0, self._reflect_update)
            except Exception:
                pass

    def _reflect_update(self) -> None:
        """Show the update link on the current screen, if it supports one."""
        scr = self._current_screen
        if scr is not None and self.update_info and hasattr(scr, "show_update_indicator"):
            scr.show_update_indicator(self.update_info)

    # -----------------------------------------------------------------------

    def show_screen(self, name: str) -> None:
        """Destroy the current screen frame and show a new one."""
        # Destroy previous screen (release its keyboard shortcuts first)
        if self._current_screen is not None:
            T.unbind_shortcuts(self._current_screen)
            self._current_screen.destroy()
            self._current_screen = None

        # Resize window
        geom = _GEOMETRY.get(name, "700x700")
        self.geometry(geom)

        # Instantiate and pack the new screen
        ScreenClass = _load_screen(name)
        screen = ScreenClass(self._container, self)
        screen.pack(fill="both", expand=True)
        self._current_screen = screen


def main():
    app = SEToolsApp()
    app.mainloop()


def _check(outfile: str) -> None:
    """Headless smoke test used by CI: build the app and every screen without
    showing a window, then write the result to *outfile* (a windowed exe has no
    console, so the outcome is written to a file the workflow can read)."""
    try:
        app = SEToolsApp()
        app.withdraw()
        app.update_idletasks(); app.update()
        for name in ("setup", "image_converter", "text_converter", "home"):
            app.show_screen(name)
            app.update_idletasks(); app.update()
        app.destroy()
        result = "RESULT=OK"
    except Exception:
        import traceback
        result = "RESULT=FAIL\n" + traceback.format_exc()
    try:
        with open(outfile, "w", encoding="utf-8") as fh:
            fh.write(result)
    except Exception:
        pass


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--check":
        _check(sys.argv[2])
    else:
        main()
