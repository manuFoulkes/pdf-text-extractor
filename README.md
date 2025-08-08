# PDF Text Extractor

Aplicación de escritorio para extraer texto de PDFs escaneados usando OCR (Tesseract).

### Para usuarios finales (Windows)
- Descarga e instala el archivo del instalador (`PDFTextExtractor_Setup.exe`) desde la sección de Releases o la carpeta `Output`.
- No se requieren dependencias externas: el instalador incluye Tesseract y Poppler.

### Para desarrolladores
#### Clonar y entorno
```bash
git clone https://github.com/manuFoulkes/pdf-text-extractor.git
cd pdf-text-extractor
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### Ejecutar la app en modo desarrollo
```bash
python src/app.py
```
- Si en el proyecto existen las carpetas `Tesseract-OCR` y `poppler`, la app las usará automáticamente.
- Alternativamente, puedes instalar Tesseract/Poppler en el sistema (solo para desarrollo).

#### Ejecutar tests
```bash
venv\Scripts\python -m pytest
```

### Crear ejecutable e instalador (Windows)
Opción 1: script automático
```bat
build_installer.bat
```
- Genera `dist\PDFTextExtractor\` (app + dependencias) y el instalador en `Output\PDFTextExtractor_Setup.exe`.

Opción 2: pasos manuales
```bat
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install -r requirements.txt
venv\Scripts\python -m pip install pyinstaller
venv\Scripts\pyinstaller --noconfirm --clean pdf_extractor.spec
```
- Abre y compila `installer.iss` con Inno Setup (ISCC). El instalador se genera en `Output`.

Notas
- El paquete incluye `resources\spa.traineddata`. En el primer arranque se copia a `Tesseract-OCR\tessdata` si falta.
- El ejecutable principal es `PDFTextExtractor.exe` (en `dist\PDFTextExtractor` o en la carpeta de instalación del programa).
