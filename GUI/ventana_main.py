import hashlib
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil
from tkinter import messagebox
from GUI.graficas import generar_graficos_desde_excel   # Importa la función desde el módulo graficos.py

class VentanaPrincipal:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Análisis de datos mediante Excel")

        # Crear el directorio 'Data' si no existe
        self.crear_directorio_data()

        # Calcula las dimensiones de la pantalla
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calcula las dimensiones y posición de la ventana
        window_width = 400  # Ancho de la ventana
        window_height = 400  # Alto de la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establece la geometría de la ventana para centrarla
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Botón para cargar archivo Excel
        self.btn_cargar_excel = ttk.Button(master, text="Subir Archivo Excel", command=self.subir_archivo_excel)
        self.btn_cargar_excel.pack(pady=20)

        # Marco para mostrar nombres de archivos subidos
        self.marco_archivos = ttk.Frame(master)
        self.marco_archivos.pack(side="bottom", fill="both", pady=20)

        # Botón para generar gráficos
        self.btn_generar_graficos = ttk.Button(master, text="Generar Gráficos", command=self.generar_graficos)
        self.btn_generar_graficos.pack(pady=20)

        # Lista de archivos subidos
        self.archivos_subidos = []

        # Cargar y mostrar los nombres de archivos en la carpeta "Data"
        self.actualizar_archivos_subidos()

    def crear_directorio_data(self):
        # Obtener la ruta del directorio 'Data' relativa al directorio del script
        directorio_actual = os.path.dirname(__file__)
        directorio_data = os.path.join(directorio_actual, 'Data')

        # Verificar si el directorio 'Data' no existe
        if not os.path.exists(directorio_data):
            # Crear el directorio 'Data'
            os.makedirs(directorio_data)
            print("Directorio 'Data' creado correctamente.")
        else:
            print("El directorio 'Data' ya existe.")
    def subir_archivo_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
        if filepath:
            nombre_archivo = os.path.basename(filepath)
            directorio_data = os.path.join(os.path.dirname(__file__), 'Data', nombre_archivo)
            if os.path.exists(directorio_data) and os.path.samefile(filepath, directorio_data):
                messagebox.showwarning("Archivo Existente", f"El archivo '{nombre_archivo}' ya existe en la carpeta 'Data'. No se puede subir porque es el mismo archivo.")
            elif os.path.exists(directorio_data):
                respuesta = messagebox.askyesno("Archivo Existente", f"El archivo '{nombre_archivo}' ya existe en la carpeta 'Data'. ¿Desea reemplazarlo?")
                if respuesta:
                    shutil.copyfile(filepath, directorio_data)
                    self.actualizar_archivos_subidos()
                    messagebox.showinfo("Archivo Reemplazado", f"El archivo '{nombre_archivo}' se ha reemplazado con éxito en la carpeta 'Data'.")
            else:
                shutil.copyfile(filepath, directorio_data)
                self.actualizar_archivos_subidos()
                messagebox.showinfo("Archivo Subido", f"El archivo '{nombre_archivo}' se ha subido con éxito a la carpeta 'Data'.")


    def calcular_hash(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def eliminar_archivo(self, nombre_archivo):
        try:
            # Eliminar el archivo de la carpeta "Data"
            directorio_actual = os.path.dirname(__file__)
            os.remove(os.path.join(directorio_actual, 'Data', nombre_archivo))
            # Actualizar la lista de archivos subidos
            self.actualizar_archivos_subidos()
        except PermissionError:
            messagebox.showwarning("Error al eliminar archivo", f"No se puede eliminar el archivo '{nombre_archivo}' porque está siendo utilizado por otro proceso.")
        except FileNotFoundError:
            pass

    def actualizar_archivos_subidos(self):
        # Limpiar la lista de archivos subidos
        for widget in self.marco_archivos.winfo_children():
            widget.destroy()
        self.archivos_subidos.clear()
        # Obtener la lista de archivos en la carpeta "Data"
        directorio_actual = os.path.dirname(__file__)
        archivos_data = os.listdir(os.path.join(directorio_actual, 'Data'))
        # Mostrar los nombres de archivos en la ventana principal
        for archivo in archivos_data:
            btn_eliminar = ttk.Button(self.marco_archivos, text=f"Eliminar {archivo}", command=lambda nombre=archivo: self.eliminar_archivo(nombre))
            btn_eliminar.pack(side="bottom", anchor="w")
            self.archivos_subidos.append(archivo)

    def generar_graficos(self):
        # Diálogo para seleccionar el archivo del cual se desea generar gráficos
        selected_file = filedialog.askopenfilename(initialdir=os.path.join(os.path.dirname(__file__), 'Data'), title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
        if selected_file:
            generar_graficos_desde_excel(selected_file)  # Llama a la función para generar los gráficos

def main():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()