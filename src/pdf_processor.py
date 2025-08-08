import os
from pdf2image import convert_from_path
import pytesseract
try:
    from .utils import setup_environment  # import relativo cuando se usa como paquete
except Exception:
    from utils import setup_environment  # fallback cuando se ejecuta desde src/
from PIL import Image

class PDFProcessor:
    def __init__(self, progress_callback=None):
        self.progress_callback = progress_callback
        print("Inicializando PDFProcessor...")  # Debug
        
        # Verificar que Tesseract esté instalado y accesible
        try:
            # Asegurar variables de entorno para ejecución empaquetada
            setup_environment()
            version = pytesseract.get_tesseract_version()
            print(f"Tesseract version: {version}")  # Debug
        except Exception as e:
            print(f"Error al verificar Tesseract: {str(e)}")  # Debug
            raise Exception("Tesseract no está instalado o no está en el PATH del sistema. Error: " + str(e))

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
        try:
            # Verificar que el archivo existe
            if not os.path.exists(pdf_path):
                raise Exception(f"El archivo PDF no existe: {pdf_path}")
            
            print(f"Procesando archivo: {pdf_path}")  # Debug
            
            # Convertir PDF a imágenes
            self.update_progress(0.1, "Convirtiendo PDF a imágenes...")
            try:
                images = convert_from_path(pdf_path)
                print(f"PDF convertido a {len(images)} imágenes")  # Debug
            except Exception as e:
                print(f"Error al convertir PDF: {str(e)}")  # Debug
                if "poppler" in str(e).lower():
                    raise Exception("Error: Poppler no está instalado o no está en el PATH del sistema. Por favor, instala Poppler y asegúrate de que esté en el PATH.")
                raise
            
            # Crear archivo de texto
            with open(output_path, 'w', encoding='utf-8') as f:
                total_pages = len(images)
                print(f"Comenzando procesamiento de {total_pages} páginas")  # Debug
                
                # Procesar cada página
                for i, image in enumerate(images, 1):
                    self.update_progress(
                        (i / total_pages) * 0.9 + 0.1,
                        f"Procesando página {i} de {total_pages}..."
                    )
                    
                    # Extraer texto de la imagen
                    try:
                        # Intentar primero con español, si falla usar inglés
                        try:
                            text = pytesseract.image_to_string(image, lang='spa')
                        except Exception:
                            print("Advertencia: No se pudo usar el idioma español, usando inglés como alternativa")
                            text = pytesseract.image_to_string(image, lang='eng')
                    except Exception as e:
                        raise Exception(f"Error al extraer texto de la página {i}. Verifica que Tesseract esté instalado correctamente. Error: {str(e)}")
                    
                    # Escribir texto en el archivo
                    f.write(f"=== Página {i} ===\n\n")
                    f.write(text)
                    f.write('\n\n')
                    
                    # Liberar memoria
                    image.close()
                    
        except Exception as e:
            if "convert_from_path" in str(e):
                raise Exception(f"Error al convertir PDF a imágenes. Asegúrate de que Poppler esté instalado correctamente. Error: {str(e)}")
            raise Exception(f"Error durante el procesamiento del PDF: {str(e)}")
