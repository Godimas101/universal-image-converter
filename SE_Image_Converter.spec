# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for SE Image Converter — ONEDIR build.
#
# Onedir (not onefile): the DLLs live in the install folder instead of being
# unpacked to %TEMP% on every launch. A onefile exe is a single self-extracting
# blob that trips Windows Defender's packer heuristic (false-positive "virus")
# and races Defender on the temp extraction; onedir avoids both. The Inno
# installer packages the whole dist\SE Image Converter\ folder.
#
# Build:  pyinstaller SE_Image_Converter.spec   (or run build.bat)

from PyInstaller.utils.hooks import collect_all

# Collect all Pillow components (image format plugins, libs, etc.)
pil_datas, pil_binaries, pil_hiddenimports = collect_all("PIL")

a = Analysis(
    ["se_launcher.py"],
    pathex=[],
    binaries=pil_binaries,
    datas=pil_datas + [("VERSION", ".")],
    hiddenimports=pil_hiddenimports + [
        # Screen modules are loaded lazily by string name in se_launcher.py
        # so PyInstaller won't detect them via static analysis.
        "screen_home",
        "screen_setup",
        "screen_image_converter",
        "screen_text_converter",
        # Tool logic modules
        "se_theme",
        "se_lcd_convert",
        "se_text_convert",
        # tkinter — usually auto-detected, listed explicitly for safety
        "tkinter",
        "tkinter.ttk",
        "tkinter.filedialog",
        "tkinter.colorchooser",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,        # onedir: binaries go into the COLLECT folder
    name="SE Image Converter",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,      # no console window — GUI only
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="icon.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="SE Image Converter",
)
