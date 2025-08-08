#define MyAppName "PDF Text Extractor"
#define MyAppVersion "1.0"
#define MyAppPublisher "Your Name"
#define MyAppExeName "PDFTextExtractor.exe"

[Setup]
AppId={{PDF-TEXT-EXTRACTOR-2025}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
; Instalar en Program Files de 64 bits y marcar instalador como x64
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
DefaultDirName={pf64}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputBaseFilename=PDFTextExtractor_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
DisableDirPage=no
DisableProgramGroupPage=no

[Files]
; Archivos principales de la aplicación (build de PyInstaller carpeta)
Source: "dist\PDFTextExtractor\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; Recursos
Source: "resources\*"; DestDir: "{app}\resources"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "{app}\PDFTextExtractor.exe"; Description: "Ejecutar la aplicación"; Flags: postinstall nowait skipifsilent

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\PDFTextExtractor.exe"; WorkingDir: "{app}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\PDFTextExtractor.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; Flags: unchecked

[Code]

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    { El instalador ha terminado }
  end;
end;
