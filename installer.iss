; Version is supplied by the build (CI + build.bat pass it from the VERSION
; file):  ISCC /DAppVer=1.2.3 installer.iss  — falls back to the default below.
#ifndef AppVer
  #define AppVer "1.6.0"
#endif

[Setup]
AppName=SE Image Converter
AppVersion={#AppVer}
AppPublisher=Godimas
AppPublisherURL=https://patreon.com/Godimas101
AppSupportURL=https://github.com/Godimas101/universal-image-converter
DefaultDirName={localappdata}\SEImageConverter
DefaultGroupName=SE Image Converter
DisableProgramGroupPage=yes
OutputDir=installer
OutputBaseFilename=SEImageConverterSetup-v{#AppVer}
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\SE Image Converter.exe
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Onedir build: package the whole PyInstaller output folder (exe + _internal).
Source: "dist\SE Image Converter\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SE Image Converter"; Filename: "{app}\SE Image Converter.exe"
Name: "{group}\Uninstall SE Image Converter"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\SE Image Converter.exe"; Description: "Launch SE Image Converter now"; Flags: nowait postinstall skipifsilent
