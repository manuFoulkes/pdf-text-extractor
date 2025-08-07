import os
import threading
from tkinter import filedialog
import customtkinter as ctk
from pdf_processor import PDFProcessor

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar ventana
        self.title("PDF Text Extractor")
        self.geometry("600x400")
        
        # Configurar tema
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Variables
        self.pdf_path = None
        self.output_dir = None

        # Crear interfaz
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        title = ctk.CTkLabel(main_frame, text="PDF Text Extractor", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        # Botón seleccionar PDF
        self.pdf_button = ctk.CTkButton(
            main_frame,
            text="Seleccionar PDF",
            command=self.select_pdf
        )
        self.pdf_button.pack(pady=10)

        # Label para mostrar el archivo seleccionado
        self.pdf_label = ctk.CTkLabel(main_frame, text="Ningún archivo seleccionado")
        self.pdf_label.pack(pady=5)

        # Botón seleccionar carpeta destino
        self.dir_button = ctk.CTkButton(
            main_frame,
            text="Seleccionar Carpeta Destino",
            command=self.select_output_dir
        )
        self.dir_button.pack(pady=10)

        # Label para mostrar la carpeta seleccionada
        self.dir_label = ctk.CTkLabel(main_frame, text="Ninguna carpeta seleccionada")
        self.dir_label.pack(pady=5)

        # Barra de progreso
        self.progress_bar = ctk.CTkProgressBar(main_frame)
        self.progress_bar.pack(pady=20, fill="x", padx=40)
        self.progress_bar.set(0)

        # Label para mostrar el estado
        self.status_label = ctk.CTkLabel(main_frame, text="")
        self.status_label.pack(pady=5)

        # Botón procesar
        self.process_button = ctk.CTkButton(
            main_frame,
            text="Procesar PDF",
            command=self.process_pdf,
            state="disabled"
        )
        self.process_button.pack(pady=10)

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        if self.pdf_path:
            self.pdf_label.configure(text=os.path.basename(self.pdf_path))
            self.check_ready()

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()
        if self.output_dir:
            self.dir_label.configure(text=self.output_dir)
            self.check_ready()

    def check_ready(self):
        if self.pdf_path and self.output_dir:
            self.process_button.configure(state="normal")
        else:
            self.process_button.configure(state="disabled")

    def update_progress(self, progress, status):
        self.progress_bar.set(progress)
        self.status_label.configure(text=status)

    def process_pdf(self):
        # Deshabilitar botones durante el proceso
        self.process_button.configure(state="disabled")
        self.pdf_button.configure(state="disabled")
        self.dir_button.configure(state="disabled")

        # Crear instancia del procesador
        processor = PDFProcessor(self.update_progress)

        # Procesar PDF en un hilo separado
        thread = threading.Thread(
            target=self._process_pdf_thread,
            args=(processor,)
        )
        thread.start()

    def _process_pdf_thread(self, processor):
        try:
            # Obtener nombre base del archivo
            base_name = os.path.splitext(os.path.basename(self.pdf_path))[0]
            output_path = os.path.join(self.output_dir, f"{base_name}.txt")

            # Procesar PDF
            processor.process_pdf(self.pdf_path, output_path)

            # Actualizar UI al terminar
            self.status_label.configure(text="¡Proceso completado!")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
        finally:
            # Re-habilitar botones
            self.process_button.configure(state="normal")
            self.pdf_button.configure(state="normal")
            self.dir_button.configure(state="normal")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
