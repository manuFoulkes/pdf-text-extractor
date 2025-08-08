# PDF Text Extractor

Una aplicación de escritorio simple para extraer texto de archivos PDF escaneados usando OCR.

## Requisitos previos

1. Python 3.8 o superior
2. Tesseract OCR
3. Poppler

### Instalación de dependencias

1. **Tesseract OCR**:
   - Windows: Descarga e instala desde [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

2. **Poppler**:
   - Windows: Descarga e instala desde [http://blog.alivate.com.au/poppler-windows/](http://blog.alivate.com.au/poppler-windows/)
   - Linux: `sudo apt-get install poppler-utils`
   - macOS: `brew install poppler`

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/yourusername/pdf-text-extractor.git
   cd pdf-text-extractor
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecutar la aplicación:
   ```bash
   python src/app.py
   ```

2. Usar la interfaz gráfica para:
   - Seleccionar un archivo PDF
   - Elegir la carpeta de destino
   - Hacer clic en "Procesar PDF"

## Crear ejecutable e instalador

1. Instalar PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Crear el ejecutable (carpeta):
   ```bash
    pyinstaller --clean --noconfirm pdf_extractor.spec
   ```
    Esto genera la carpeta `dist/PDFTextExtractor` que incluye la app, `Tesseract-OCR`, `poppler` y `resources`.

3. Crear instalador (Inno Setup):
    - Instala Inno Setup.
    - Abre `installer.iss` y compílalo, o ejecuta Inno Setup desde línea de comando apuntando a `installer.iss`.
