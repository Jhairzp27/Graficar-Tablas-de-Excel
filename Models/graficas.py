# Models/graficas.py

import tkinter as tk
from tkinter import ttk

def generar_graficos_desde_excel(filepath):
    # Función para generar gráficos a partir de un archivo Excel
    # Esta función se encarga de mostrar la ventana emergente para seleccionar las opciones de gráfico
    # y luego llama a la función correspondiente para generar los gráficos

    # Crear la ventana emergente para seleccionar opciones
    ventana_opciones = tk.Toplevel()
    ventana_opciones.title("Selección de Opciones")

    # Calcula las dimensiones de la pantalla
    screen_width = ventana_opciones.winfo_screenwidth()
    screen_height = ventana_opciones.winfo_screenheight()

    # Calcula las dimensiones y posición de la ventana emergente
    window_width = 350  # Ancho de la ventana
    window_height = 200  # Alto de la ventana
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establece la geometría de la ventana emergente para centrarla
    ventana_opciones.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Etiqueta para instrucciones
    lbl_instrucciones = ttk.Label(ventana_opciones, text="Seleccione el tipo de unidad:")
    lbl_instrucciones.grid(row=0, column=0, padx=10, pady=5)

    # Menú desplegable para seleccionar el tipo de unidad
    combo_tipo_unidad = ttk.Combobox(ventana_opciones, values=["Grandes", "Micros"], state="readonly")
    combo_tipo_unidad.grid(row=0, column=1, padx=10, pady=5)
    combo_tipo_unidad.current(0)  # Seleccionar el primer elemento por defecto

    def mostrar_opciones_num_unidad():
        # Función para mostrar las opciones de número de unidad según el tipo seleccionado

        # Obtener el tipo de unidad seleccionado
        tipo_unidad = combo_tipo_unidad.get()

        # Eliminar widgets existentes de opciones de número de unidad (si hay alguno)
        for widget in ventana_opciones.winfo_children():
            if isinstance(widget, ttk.LabelFrame):
                widget.destroy()

        # Mostrar las opciones de número de unidad correspondientes
        lbl_frame_num_unidad = ttk.LabelFrame(ventana_opciones, text="Seleccione el número de unidad:")
        lbl_frame_num_unidad.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        if tipo_unidad == "Grandes":
            opciones_num_unidad = ["1", "2", "3"]  # Ejemplo de opciones para unidades Grandes
        elif tipo_unidad == "Micros":
            opciones_num_unidad = ["A", "B", "C"]  # Ejemplo de opciones para Micros

        combo_num_unidad = ttk.Combobox(lbl_frame_num_unidad, values=opciones_num_unidad, state="readonly")
        combo_num_unidad.pack(padx=10, pady=5)

    # Botón para mostrar las opciones de número de unidad
    btn_mostrar_opciones = ttk.Button(ventana_opciones, text="Mostrar Opciones", command=mostrar_opciones_num_unidad)
    btn_mostrar_opciones.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Función para generar los gráficos con las opciones seleccionadas
    def generar_graficos_con_opciones():
        tipo_unidad = combo_tipo_unidad.get()
        num_unidad = combo_num_unidad.get()
        # Aquí puedes llamar a la función para generar los gráficos con las opciones seleccionadas
        print(f"Generar gráficos para unidad {tipo_unidad} {num_unidad}")

    # Botón para generar los gráficos con las opciones seleccionadas
    btn_generar_graficos = ttk.Button(ventana_opciones, text="Generar Gráficos", command=generar_graficos_con_opciones)
    btn_generar_graficos.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    ventana_opciones.mainloop()
