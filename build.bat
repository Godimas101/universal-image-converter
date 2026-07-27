@echo off
:: ============================================================
:: SE Image Converter — build script (onedir + Inno installer)
:: Output:  installer\SEImageConverterSetup-v<VERSION>.exe
:: ============================================================
setlocal
set /p APPVER=<VERSION

python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found. Install Python 3.8+ and add it to PATH.
    pause & exit /b 1
)

echo  Installing dependencies...
pip install --quiet --upgrade -r requirements.txt pyinstaller

echo  Building onedir app...
python -m PyInstaller SE_Image_Converter.spec --clean --noconfirm
if errorlevel 1 (
    echo  BUILD FAILED. Check the output above for errors.
    pause & exit /b 1
)

set ISCC=
for %%p in (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
    "C:\Program Files\Inno Setup 6\ISCC.exe"
) do if exist %%p set ISCC=%%p

if "%ISCC%"=="" (
    echo  Built onedir app: dist\SE Image Converter\   ^(Inno Setup not found — skipping installer^)
    pause & exit /b 0
)

%ISCC% /DAppVer=%APPVER% installer.iss
echo.
echo  ============================================================
echo   Build complete:  installer\SEImageConverterSetup-v%APPVER%.exe
echo  ============================================================
pause
