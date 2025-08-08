@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Build script: creates venv, installs deps, builds PyInstaller dist and Inno Setup installer

REM 1) Ensure venv
if not exist venv (
  py -m venv venv || (
    echo Failed to create virtualenv
    exit /b 1
  )
)

REM 2) Upgrade pip and install deps
call venv\Scripts\python -m pip install --upgrade pip
call venv\Scripts\python -m pip install -r requirements.txt
call venv\Scripts\python -m pip install pyinstaller

REM 3) Build app with PyInstaller spec
call venv\Scripts\pyinstaller --noconfirm --clean pdf_extractor.spec || (
  echo PyInstaller build failed
  exit /b 1
)

REM 4) Build installer with Inno Setup Compiler (ISCC)
set ISCC_PATH=
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" set ISCC_PATH="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if exist "C:\Program Files\Inno Setup 6\ISCC.exe" set ISCC_PATH="C:\Program Files\Inno Setup 6\ISCC.exe"

if "%ISCC_PATH%"=="" (
  echo Could not find Inno Setup Compiler (ISCC.exe).
  echo Please install Inno Setup 6 and re-run this script.
  echo Download: https://jrsoftware.org/isdl.php
  exit /b 1
)

%ISCC_PATH% installer.iss || (
  echo Inno Setup build failed
  exit /b 1
)

echo.
echo Build completed. Installer should be in the Output folder.
exit /b 0


