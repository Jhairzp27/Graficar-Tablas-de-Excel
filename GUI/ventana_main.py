import os
import shutil
import customtkinter as ctk
from tkinter import filedialog
from GUI.dialogos import mostrar_dialogo_centrado
from GUI.graficas import generar_graficos_desde_excel

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
         # Calcular dimensiones para centrar la ventana
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configurar geometría con las coordenadas calculadas
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        ctk.set_appearance_mode("dark")  # Modo oscuro
        ctk.set_default_color_theme("dark-blue")  # Tema predeterminado

        # Título principal
        titulo = ctk.CTkLabel(self, text="📊 Análisis de Datos Excel", font=("Segoe UI", 20, "bold"))
        titulo.pack(pady=20)

        # Botón para subir archivo Excel
        self.btn_cargar_excel = ctk.CTkButton(
            self,
            text="📂 Subir Archivo Excel",
            fg_color="#4a90e2",  # Color de fondo
            hover_color="#ff9800",  # Color al pasar el cursor
            text_color="white",
            command=self.subir_archivo_excel
        )
        self.btn_cargar_excel.pack(pady=20)

        # Marco para archivos subidos
        self.marco_archivos = ctk.CTkFrame(self, fg_color="#282a36", corner_radius=10)
        self.marco_archivos.pack(pady=10, fill="x", padx=20)

        # Botón para generar gráficos
        self.btn_generar_graficos = ctk.CTkButton(
            self,
            text="📈 Generar Gráficos",
            fg_color="#4a90e2",
            hover_color="#ff9800",
            text_color="white",
            command=self.generar_graficos
        )
        self.btn_generar_graficos.pack(pady=20)

        # Lista de archivos subidos
        self.archivos_subidos = []
        self.actualizar_archivos_subidos()

    def subir_archivo_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
        if filepath:
            nombre_archivo = os.path.basename(filepath)
            directorio_data = os.path.join(os.getcwd(), "Data", nombre_archivo)
            os.makedirs("Data", exist_ok=True)
            if os.path.exists(directorio_data):
                respuesta = mostrar_dialogo_centrado("warning","Archivo Existente",f"El archivo: '{nombre_archivo}' ya existe. \n¿Desea reemplazarlo?")
                if respuesta:
                    shutil.copyfile(filepath, directorio_data)
            else:
                shutil.copyfile(filepath, directorio_data)
            self.actualizar_archivos_subidos()

    def actualizar_archivos_subidos(self):
        # Limpiar widgets anteriores
        for widget in self.marco_archivos.winfo_children():
            widget.destroy()

        # Mostrar archivos en la carpeta "Data"
        data_dir = os.path.join(os.getcwd(), "Data")
        os.makedirs(data_dir, exist_ok=True)
        archivos = os.listdir(data_dir)

        for archivo in archivos:
            marco_individual = ctk.CTkFrame(self.marco_archivos, fg_color="#3b3f51", corner_radius=5)
            marco_individual.pack(fill="x", pady=5, padx=5)

            etiqueta = ctk.CTkLabel(marco_individual, text=archivo, text_color="white")
            etiqueta.pack(side="left", padx=10)

            btn_eliminar = ctk.CTkButton(
                marco_individual,
                text="🗑️ Eliminar",
                width=100,
                fg_color="#d9534f",
                hover_color="#c9302c",
                text_color="white",
                command=lambda nombre=archivo: self.eliminar_archivo(nombre)
            )
            btn_eliminar.pack(side="right", padx=10)

    def eliminar_archivo(self, nombre_archivo):
        try:
            data_dir = os.path.join(os.getcwd(), "Data", nombre_archivo)
            os.remove(data_dir)
            self.actualizar_archivos_subidos()
        except Exception as e:
            mostrar_dialogo_centrado("error", "Error al eliminar",f"No se pudo eliminar el archivo: \n{e}")

    def generar_graficos(self):
        selected_file = filedialog.askopenfilename(
            initialdir=os.path.join(os.getcwd(), 'Data'),
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")]
        )
        if selected_file:
            generar_graficos_desde_excel(selected_file)
