import openpyxl
from tkinter import filedialog

def cargar_excel(self):
    # Diálogo para seleccionar archivo Excel
    filepath = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
    if filepath:
        # Procesar el archivo Excel
        workbook = openpyxl.load_workbook(filepath)
        # Aquí puedes agregar la lógica para crear gráficos basados en las páginas del archivo Excel
        print("Archivo Excel cargado:", filepath)