# AGENTS.md — universal-image-converter

Windows tool for Space Engineers modders. Converts images to `.dds` textures for LCD mods, and generates pasteable LCD text strings for in-game art. Distributed as a packaged `.exe` via GitHub Releases.

## What this is

Windows tool for Space Engineers modders. Converts images to `.dds` textures for LCD mods, and generates pasteable LCD text strings for in-game art. Distributed as a packaged `.exe` via GitHub Releases.

## Where work lives (RULE — non-negotiable)

**Every task on this repo is a ticket on the [Personal Projects board](https://github.com/users/Godimas101/projects/2).** YOU (the agent) create the ticket BEFORE touching anything. No exceptions for "small" work.

Concrete rules — same as everywhere:

- **Starting work?** Open a ticket, add to the board, set Status = **In Progress**, then start.
- **Have an idea for later?** Ticket in **Backlog**. Not in memory, not in a README, not in NOTES.md.
- **Need Chris to check something before closing?** Move to **In QA** and comment what he needs to look at. Do NOT set to Done — that's Chris's call after review.
- **Finished + verified yourself?** Close the ticket with a closing summary (what you did / problems + solutions / anything NOT done).
- **Same-session micro-work?** Open + close in the same session — but the ticket exists.
- **Older than 30 days in Done?** The weekly cron moves it to Archived. The closed ticket persists.

Ticket body shape: see memory `[[feedback-ticket-body-shape]]` — What/Why → Acceptance → Related → Notes. Priority defaults to P2, Kind defaults to Feature.

## How to verify (before flagging In QA or closing)

- Test with real images (PNG + JPG at least) — the DDS output should load in-game without crashing SE.
- If touching the LCD-string generator, paste output into a real SE LCD and verify it renders correctly.
- Check that the packaged `.exe` still runs standalone (no missing dependencies) after any build change.
- If touching texconv integration: verify graceful fallback when `texconv.exe` isn't found (should degrade, not crash).

## MUST NOT

- Break the packaged `.exe` — this is a Released app; users grab the exe and expect it to work.
- Hardcode texconv paths — it's an optional dependency users provide.
- Modify sample images in `docs/` — those are documentation, not test fixtures.

## Related

- Sibling tool: [`universal-audio-converter`](https://github.com/Godimas101/universal-audio-converter)
- Bundled by: [`space-engineers-modders-tool-kit`](https://github.com/Godimas101/space-engineers-modders-tool-kit)

---

*Part of Chris's `Godimas101` personal repos. Companion guide: `personal-docs/git-infrastructure.md` (private companion repo) covers the full infrastructure.*