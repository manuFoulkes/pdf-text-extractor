import os
import sys

def get_base_path():
    """
    Obtiene la ruta base de la aplicación, funcionando tanto en modo desarrollo
    como cuando se ejecuta desde el ejecutable de PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        # Ejecutando en un bundle (PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # Ejecutando en modo desarrollo
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_resource_path(relative_path):
    """
    Obtiene la ruta absoluta a un recurso, funcionando tanto en modo desarrollo
    como cuando se ejecuta desde el ejecutable de PyInstaller.
    """
    base_path = get_base_path()
    return os.path.join(base_path, 'resources', relative_path)

def setup_environment():
    """
    Configura las variables de entorno necesarias para Tesseract y Poppler.
    """
    base_path = get_base_path()
    
    # Configurar Tesseract
    tesseract_path = os.path.join(base_path, 'Tesseract-OCR')
    if os.path.exists(tesseract_path):
        os.environ['PATH'] = tesseract_path + os.pathsep + os.environ.get('PATH', '')
        tessdata_dir = os.path.join(tesseract_path, 'tessdata')
        os.environ['TESSDATA_PREFIX'] = tessdata_dir

        # Asegurar que el idioma español esté presente si empaquetamos spa.traineddata
        try:
            spa_src = os.path.join(base_path, 'resources', 'spa.traineddata')
            if os.path.exists(spa_src):
                os.makedirs(tessdata_dir, exist_ok=True)
                spa_dst = os.path.join(tessdata_dir, 'spa.traineddata')
                if not os.path.exists(spa_dst):
                    # Copiar archivo de datos de idioma al primer arranque
                    with open(spa_src, 'rb') as fsrc, open(spa_dst, 'wb') as fdst:
                        fdst.write(fsrc.read())
        except Exception:
            # No bloquear el arranque si falla la copia
            pass
    
    # Configurar Poppler
    poppler_path = os.path.join(base_path, 'poppler', 'bin')
    if os.path.exists(poppler_path):
        os.environ['PATH'] = poppler_path + os.pathsep + os.environ.get('PATH', '')
