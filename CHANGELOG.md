# Changelog

All notable changes to SE Universal Image Converter. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

- lcd support for billboards ([#3](https://github.com/Godimas101/universal-image-converter/issues/3)) — closed 2026-07-28 by @Godimas101
- Embed an in-app Report-a-bug link ([#5](https://github.com/Godimas101/universal-image-converter/issues/5)) — closed 2026-07-25 by @Godimas101
- CI: auto-build + publish the .exe on merge to main ([#4](https://github.com/Godimas101/universal-image-converter/issues/4)) — closed 2026-07-25 by @Godimas101

## [1.6.2] — 2026-07-26

### Added
- **Billboard preset** for the Economy 2 blocks: a "Billboard · 3:5" screen preset (covers both the Billboard and Round Billboard) in the Image → DDS and Image → LCD converters. ([#3](https://github.com/Godimas101/universal-image-converter/issues/3))

## [1.6.1] — 2026-07-26

### Changed
- The in-app **Report a bug** link now opens a pre-filled bug form with the `bug` label already applied, instead of a blank issue. Added repo issue templates (bug + feature) to back it.

## [1.6.0] — 2026-07-26

### Changed
- **Now ships as an installer, with one-click updates.** The app is built as a onedir bundle (which fixes a Windows Defender false-positive that flagged the old single-exe) and installs per-user — no admin, a Start Menu shortcut, and a clean uninstall. When a newer version exists, the home-screen notice becomes **⬆ Update & restart**: one click downloads it, installs silently, and relaunches the app. Running from source, it still just opens the release page.

## [1.5.1] — 2026-07-26

### Added
- **Update available** link on the home screen — on launch the app checks GitHub for a newer release and, if there is one, shows an "Update v*x.y.z*" link that opens the release page. Runs in the background and fails silent when offline.
- The displayed version now reads from the bundled `VERSION` file, so it can't drift from the release CI ships.

## [1.5.0] — 2026-07-25

A look-and-feel and usability refresh, matching the rest of the SE tools. Same features, same colours — cleaner type, keyboard shortcuts, and clearer feedback.

### Changed
- Refreshed the interface to the modernised SE-tool style: a clean sans typeface for headings, labels and buttons, with monospace kept where it earns its place — logs, file lists, specs, the LCD reference table and generated text-art output. The colour palette is unchanged.
- Convert now stays disabled until an image is selected, and shows a working state while it's busy.
- The "ⓘ" help button now sits in every screen's header, next to Back, and lists that screen's keyboard shortcuts.

### Added
- Keyboard shortcuts throughout — Ctrl+O to add images, Enter to convert, digit keys to jump between screens from the home page, Esc to go back, and F1 for help.
- A visible focus ring so keyboard navigation is easy to follow.
- A "Found a bug? Report it" link on the home screen.

### Fixed
- Batch conversions now report a summary (converted / failed) when they finish.
- Custom width/height values are bounds-checked so an extreme size can't exhaust memory.

## [1.4] — 2026-04-04

- Earlier release (Image → DDS / LCD conversion and text-art generation).
