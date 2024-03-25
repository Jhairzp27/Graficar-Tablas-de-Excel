import pandas as pd
import matplotlib.pyplot as plt
import locale

def generar_grafico_vueltas_semanal(filepath, tipo_unidad, num_unidad, ax=None):
    # Establecer el formato numérico
    locale.setlocale(locale.LC_NUMERIC, '')

    ylabel = None
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='PlantillaVueltas')

    # Obtener el rango de filas según el tipo de unidad
    if tipo_unidad == "Grandes":
        rango_filas = (3, 29)
        ylabel = 'Número de Vueltas'
        title = 'Vueltas L-V - Unidad ' + num_unidad
    elif tipo_unidad == "Micros":
        rango_filas = (29, 63)
        ylabel = 'Kilómetros Recorridos [Km]'
        title = 'Kilómetros Recorridos L-V - Unidad ' + num_unidad + '[Km]'
    else:
        print("Tipo de unidad no válido.")
        return

    # Asegurarse de que el número de unidad esté dentro de los límites permitidos
    num_unidad_int = int(num_unidad[1:])
    if num_unidad_int < 1 or num_unidad_int > rango_filas[1] - rango_filas[0] + 1:
        print(f"Número de unidad inválido para el tipo {tipo_unidad}.")
        return

    # Determinar la fila correspondiente al número de unidad
    fila_unidad = rango_filas[0] + num_unidad_int - 1

    # Verificar si el índice de fila está dentro de los límites del DataFrame
    if fila_unidad >= len(data):
        print("Índice de fila fuera de los límites del DataFrame.")
        return

    # Obtener los valores de Programadas, Promedio y Ejecutadas para la unidad seleccionada
    programadas = data.iloc[fila_unidad, 1]  # Programadas
    promedio = data.iloc[fila_unidad, 4]     # Promedio
    ejecutadas = data.iloc[fila_unidad, 7]   # Ejecutadas

    # Reemplazar NaN con ceros
    programadas = programadas if pd.notna(programadas) else 0
    promedio = promedio if pd.notna(promedio) else 0
    ejecutadas = ejecutadas if pd.notna(ejecutadas) else 0

    # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
    if ax is None:
        ax = plt.subplots()
    else:
        ax.clear()

    # Configurar las categorías, valores y etiquetas de las barras
    categorias = ['Programadas', 'Promedio/Ejecutadas', 'Ejecutadas']
    valores = [programadas, promedio, ejecutadas]
    custom_colors = ['#87d349', '#FFA500', '#f9e826']
    width = 0.3

    ax.bar(categorias, valores, color=custom_colors, width=width)

    # Agregar etiquetas a las barras con los valores numéricos formateados
    for i, valor in enumerate(valores):
        valor_formateado = locale.format_string("%.2f", valor, grouping=True)
        ax.text(i, valor, f'{valor_formateado}', ha='center', va='bottom')

    ax.set_ylabel(ylabel)
    ax.set_title(title)

    ax.margins(y=0.1)

    if ax is None:
        plt.show()
        plt.close()
