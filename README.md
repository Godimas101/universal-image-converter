<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=170&color=0:0B1021,45:0EA5E9,100:2563EB&text=Universal%20Image%20Converter&fontColor=ffffff&fontAlignY=35&fontSize=32&desc=Space%20Engineers%20LCD%20and%20texture%20art%20tools&descAlignY=57&descSize=18" />
</p>

> **"Because blank LCDs are just missed opportunities with better lighting."**

A Windows tool for Space Engineers players and modders who want images to behave themselves. It covers two very useful jobs:
- turning images into `.dds` textures for LCD mods
- turning images into pasteable LCD art for in-game screens

If you just want to use it, grab the latest build from the [GitHub Releases page](https://github.com/Godimas101/universal-image-converter/releases/latest). If you want to tinker, the Python source is here too.

## 🚀 Quick Start

1. Download `SE Image Converter.exe` from the [latest release](https://github.com/Godimas101/universal-image-converter/releases/latest)
2. Run it — no Python install is needed for the packaged app
3. Use **Image to DDS** for mod assets or **Image to LCD** for in-game art
4. Optionally place [`texconv.exe`](https://github.com/microsoft/DirectXTex/releases/latest) next to the exe for the best DDS quality

![SE Image Converter screenshot](https://i.imgur.com/HE6HNsv.png)

## ✨ Features

| Feature | What it does |
|--------|---------------|
| **Image to DDS** | Creates Space Engineers-ready `.dds` textures for LCD mods |
| **Image to LCD** | Generates pasteable LCD text strings for players |
| **Built-in screen presets** | Matches common SE LCD and cockpit aspect ratios automatically |
| **Reference helper** | Includes an in-app screen target lookup so you’re not guessing |
| **Custom mode** | Lets you dial in manual output settings when presets aren’t enough |

## 🔧 Setup

### Packaged app
- **No Python required**
- **No install required**
- just download the exe and run it

### Optional quality boost: `texconv.exe`
For **Image to DDS**, the converter works without `texconv`, but output quality is best when it’s available.

1. Download it from [DirectXTex releases](https://github.com/microsoft/DirectXTex/releases/latest)
2. Place `texconv.exe` next to `SE Image Converter.exe` or add it to your system `PATH`

---

## 🧱 Image to DDS

### Quick workflow
1. Select one or more images
2. Choose a **Screen Target**
3. Click **Convert**
4. Drop the resulting `.dds` into your mod’s `Textures/Models/` folder

### Screen targets

| Preset | Best for |
|--------|----------|
| `LCD Panel · 1:1` | LCD Panel, Transparent LCD, Holo LCD, Full Block LCD |
| `Wide LCD Panel · 2:1` | Wide LCD Panel |
| `Text Panel / Curved · ~5:3` | Text Panel, Curved LCD, many cockpit screens |
| `Widescreen · 16:9` | Vending Machine, Jukebox, Food Dispenser, Entertainment Corner |
| `Corner LCD Strip · ~6:1` | Corner LCD panels |
| `Custom` | Manual control when you want to fine-tune things |

> Click **ⓘ** in the app for the full block reference table.

### Example mod structure

```text
MyMod/
  Data/
    LCDTextures.sbc
  Textures/
    Models/
      MyImage.dds
    Sprites/
      MyImage.dds
```

### Example `LCDTextures.sbc`

```xml
<?xml version="1.0"?>
<Definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <LCDTextures>
    <LCDTextureDefinition>
      <Id>
        <TypeId>LCDTextureDefinition</TypeId>
        <SubtypeId>MyUniqueImageName</SubtypeId>
      </Id>
      <LocalizationId>MyUniqueImageName</LocalizationId>
      <TexturePath>Textures\Models\MyImage.dds</TexturePath>
      <SpritePath>Textures\Sprites\MyImage.dds</SpritePath>
      <Selectable>true</Selectable>
    </LCDTextureDefinition>
  </LCDTextures>
</Definitions>
```

---

## 📋 Image to LCD

### Quick workflow
1. Select your image
2. Choose the target screen preset
3. Pick a dithering mode — **Floyd-Steinberg** is the best default for photos
4. Click **Convert to Text**
5. Click **Copy to Clipboard**
6. In-game, paste the result into an LCD panel using these settings:

| Setting | Value |
|---------|-------|
| `Content` | `Text and Images` |
| `Font` | `Monospaced` |
| `Font Size` | use the value shown in the converter |
| `Text Padding` | `0` |

7. Click **Edit Text**, paste, and admire your extremely unnecessary but excellent screen art

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `se_launcher.py` | Main launcher for the Python version |
| `se_lcd_convert.py` | DDS conversion logic |
| `se_text_convert.py` | LCD text conversion logic |
| `screen_*.py` | UI screens for the tool |
| `build.bat` | Build helper for the packaged executable |

## 🐍 Running from Source

```bash
pip install Pillow
python se_launcher.py
```

Requires **Python 3.8+**.

## 📝 Notes

- `texconv.exe` is optional, but strongly recommended for the best DDS output quality
- the packaged exe is the easiest way to use the tool if you don’t care about the source code
- this repo covers both the modder workflow and the player-facing LCD text workflow in one place

## 🙌 Credits

Made with ♥ by **Godimas** and **Claude**.

Image-to-LCD encoding was reverse engineered from [Whiplash's Image Converter](https://github.com/Whiplash141/Whips-Image-Converter), with values cross-checked against Space Engineers tools and game files.

## 🧡 Support

This tool is free and always will be. If it saves you time on your next build, consider supporting on Patreon — it helps keep the tools and mods coming.

[![Support on Patreon](https://raw.githubusercontent.com/Godimas101/personal-projects/main/patreon/images/buttons/patreon-medium.png)](https://patreon.com/Godimas101)

*May cause an uncontrollable urge to texture every screen on your base.* 🖥️
