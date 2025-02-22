import tkinter as tk
from tkinter import ttk
from Utils.utils import obtener_opciones_desde_excel
from Models.generador_graficos import generar_graficos


def mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos):
    """
    Actualiza las opciones del segundo ComboBox basado en la selección del tipo de unidad.
    """
    tipo_unidad = combo_tipo_unidad.get()

    # Obtener las opciones desde el archivo Excel
    opciones = obtener_opciones_desde_excel(filepath, tipo_unidad)

    # Validar si hay opciones y asignarlas al ComboBox de número de unidad
    if opciones:
        combo_num_unidad['values'] = opciones
        combo_num_unidad.set(opciones[0])  # Seleccionar el primer valor por defecto
        btn_generar_graficos['state'] = tk.NORMAL  # Habilitar el botón si hay opciones
    else:
        combo_num_unidad['values'] = []
        combo_num_unidad.set("")  # Resetear el valor
        btn_generar_graficos['state'] = tk.DISABLED  # Deshabilitar el botón


def generar_graficos_desde_excel(filepath):
    def generar_graficos_seleccionados():
        """
        Función que se ejecuta al presionar el botón "Generar Gráficos".
        """
        tipo_unidad = combo_tipo_unidad.get()
        num_unidad = combo_num_unidad.get()

        if not num_unidad:
            tk.messagebox.showwarning("Advertencia", "Debe seleccionar un número de unidad.")
            return

        # Generar los gráficos con las opciones seleccionadas
        generar_graficos(filepath, tipo_unidad, num_unidad)
        tk.messagebox.showinfo("Éxito", f"Gráficos generados para la unidad {num_unidad}.")

    # Crear la ventana secundaria
    ventana_opciones = tk.Toplevel()
    ventana_opciones.title("Selección de Unidad")

    # Configurar tamaño y posición de la ventana
    window_width, window_height = 350, 200
    screen_width = ventana_opciones.winfo_screenwidth()
    screen_height = ventana_opciones.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    ventana_opciones.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_opciones.resizable(False, False)

    # Widgets para seleccionar tipo de unidad
    lbl_tipo_unidad = ttk.Label(ventana_opciones, text="Seleccione el tipo de unidad:")
    lbl_tipo_unidad.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    combo_tipo_unidad = ttk.Combobox(ventana_opciones, values=["Grandes", "Micros"], state="readonly")
    combo_tipo_unidad.grid(row=0, column=1, padx=10, pady=10)
    combo_tipo_unidad.set("Grandes")  # Seleccionar valor predeterminado

    # Widgets para seleccionar número de unidad
    lbl_num_unidad = ttk.Label(ventana_opciones, text="Seleccione el número de unidad:")
    lbl_num_unidad.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    combo_num_unidad = ttk.Combobox(ventana_opciones, state="readonly")
    combo_num_unidad.grid(row=1, column=1, padx=10, pady=10)

    # Botón para generar gráficos
    btn_generar_graficos = ttk.Button(
        ventana_opciones, text="Generar Gráficos", state=tk.DISABLED, command=generar_graficos_seleccionados
    )
    btn_generar_graficos.grid(row=2, column=0, columnspan=2, pady=10)

    # Vincular el evento del ComboBox de tipo de unidad
    def actualizar_opciones(event):
        mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos)

    combo_tipo_unidad.bind("<<ComboboxSelected>>", actualizar_opciones)

    # Cargar opciones iniciales
    mostrar_opciones_num_unidad(filepath, combo_tipo_unidad, combo_num_unidad, btn_generar_graficos)

    # Configurar la ventana como modal
    ventana_opciones.transient()
    ventana_opciones.grab_set()
    ventana_opciones.wait_window()
