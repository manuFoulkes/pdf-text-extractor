import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

class PDFProcessor:
    def __init__(self, progress_callback=None):
        self.progress_callback = progress_callback

    def update_progress(self, progress, status):
        if self.progress_callback:
            self.progress_callback(progress, status)

    def process_pdf(self, pdf_path, output_path):
        """
        Procesa un archivo PDF y extrae su texto a un archivo TXT.
        
        Args:
            pdf_path: Ruta al archivo PDF
            output_path: Ruta donde se guardará el archivo TXT
        """
        # Convertir PDF a imágenes
        self.update_progress(0.1, "Convirtiendo PDF a imágenes...")
        images = convert_from_path(pdf_path)
        
        # Crear archivo de texto
        with open(output_path, 'w', encoding='utf-8') as f:
            total_pages = len(images)
            
            # Procesar cada página
            for i, image in enumerate(images, 1):
                self.update_progress(
                    (i / total_pages) * 0.9 + 0.1,
                    f"Procesando página {i} de {total_pages}..."
                )
                
                # Extraer texto de la imagen
                text = pytesseract.image_to_string(image, lang='spa')
                
                # Escribir texto en el archivo
                f.write(f"=== Página {i} ===\n\n")
                f.write(text)
                f.write('\n\n')
