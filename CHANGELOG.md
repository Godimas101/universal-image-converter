# Changelog

All notable changes to SE Universal Image Converter. Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

- Embed an in-app Report-a-bug link ([#5](https://github.com/Godimas101/universal-image-converter/issues/5)) — closed 2026-07-25 by @Godimas101
- CI: auto-build + publish the .exe on merge to main ([#4](https://github.com/Godimas101/universal-image-converter/issues/4)) — closed 2026-07-25 by @Godimas101

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
