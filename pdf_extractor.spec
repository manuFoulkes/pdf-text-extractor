# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path

# Usar el directorio de trabajo actual como raíz del proyecto
current_dir = Path.cwd().resolve()

# Definir rutas
icon_path = (current_dir / 'resources' / 'icon.ico').resolve()
src_path = (current_dir / 'src' / 'app.py').resolve()
resources_path = (current_dir / 'resources').resolve()
tesseract_dir = (current_dir / 'Tesseract-OCR').resolve()
poppler_dir = (current_dir / 'poppler').resolve()

# Validaciones mínimas
if not icon_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo de ícono en: {icon_path}")
if not src_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo principal en: {src_path}")
if not resources_path.exists():
    raise FileNotFoundError(f"No se encontró el directorio de recursos en: {resources_path}")

print(f"Ruta del ícono: {icon_path}")
print(f"Ruta del script: {src_path}")
print(f"Ruta de recursos: {resources_path}")

block_cipher = None

# Construir lista de datos a incluir
datas = [(str(resources_path), 'resources')]
if tesseract_dir.exists():
    datas.append((str(tesseract_dir), 'Tesseract-OCR'))
if poppler_dir.exists():
    datas.append((str(poppler_dir), 'poppler'))

a = Analysis(
    [str(src_path)],
    pathex=[str(current_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'customtkinter',
        'pdf2image',
        'pytesseract',
        'PIL',
        'tkinter'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PDFTextExtractor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(icon_path)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDFTextExtractor',
)
