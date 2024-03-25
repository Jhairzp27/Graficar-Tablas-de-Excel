import tkinter as tk
from tkinter import ttk
from Utils.utils import obtener_opciones_desde_excel
from Models.generador_graficos import generar_graficos

def mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos):
    tipo_unidad = combo_tipo_unidad.get()
    num_unidad = combo_num_unidad.get()

    # Obtener las opciones desde el archivo Excel
    opciones = obtener_opciones_desde_excel(filepath, tipo_unidad)

    # Actualizar las opciones del combobox de número de unidad
    combo_num_unidad['values'] = opciones
    if num_unidad in opciones:
        combo_num_unidad.set(num_unidad)
    else:
        combo_num_unidad.set(opciones[0])  # Establecer el primer elemento por defecto

    # Actualizar el estado del botón Generar Gráficos
    if tipo_unidad and num_unidad:
        btn_generar_graficos['state'] = tk.NORMAL
    else:
        btn_generar_graficos['state'] = tk.DISABLED

def generar_graficos_desde_excel(filepath):
    def generar_graficos_seleccionados():
        tipo_unidad = combo_tipo_unidad.get()
        num_unidad = combo_num_unidad.get()
        generar_graficos(filepath, tipo_unidad, num_unidad)

    ventana_opciones = tk.Toplevel()
    ventana_opciones.title("Selección de Unidad")

    screen_width = ventana_opciones.winfo_screenwidth()
    screen_height = ventana_opciones.winfo_screenheight()

    window_width = 350
    window_height = 200
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    ventana_opciones.geometry(f"{window_width}x{window_height}+{x}+{y}")

    lbl_instrucciones = ttk.Label(ventana_opciones, text="Seleccione el tipo de unidad:")
    lbl_instrucciones.grid(row=0, column=0, padx=10, pady=5)

    combo_tipo_unidad = ttk.Combobox(ventana_opciones, values=["Grandes", "Micros"], state="readonly")
    combo_tipo_unidad.grid(row=0, column=1, padx=10, pady=5)
    combo_tipo_unidad.current(0)

    lbl_instrucciones_num_unidad = ttk.Label(ventana_opciones, text="Seleccione el número de unidad:")
    lbl_instrucciones_num_unidad.grid(row=1, column=0, padx=10, pady=5)

    combo_num_unidad = ttk.Combobox(ventana_opciones, state="readonly")
    combo_num_unidad.grid(row=1, column=1, padx=10, pady=5)

    btn_generar_graficos = ttk.Button(ventana_opciones, text="Generar Gráficos", command=generar_graficos_seleccionados, state=tk.DISABLED)
    btn_generar_graficos.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Asociar la función mostrar_opciones_num_unidad al evento de selección del tipo y número de unidad
    def actualizar_opciones_tipo_unidad(event):
        mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos)

    def actualizar_opciones_num_unidad(event):
        mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos)

    combo_tipo_unidad.bind("<<ComboboxSelected>>", actualizar_opciones_tipo_unidad)
    combo_num_unidad.bind("<<ComboboxSelected>>", actualizar_opciones_num_unidad)

    ventana_opciones.mainloop()
