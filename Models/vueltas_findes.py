import pandas as pd
import matplotlib.pyplot as plt
import locale

def generar_grafico_vueltas_findes(filepath, tipo_unidad, num_unidad, ax=None):
    # Establecer el formato numérico
    locale.setlocale(locale.LC_NUMERIC, '')

    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='PlantillaVueltas')

    # Determinar el rango de filas y columnas según el tipo de unidad
    if tipo_unidad == "Grandes":
        rango_filas = (3, 29)
        ylabel = 'Número de Vueltas'
        title = 'Vueltas S-D - Unidad ' + num_unidad
    elif tipo_unidad == "Micros":
        rango_filas = (29, 63)
        ylabel = 'Kilómetros Recorridos [Km]'
        title = 'Kilómetros Recorridos S-D - Unidad ' + num_unidad + ' [Km]'
    else:
        print("Tipo de unidad no válido.")
        return

    # Filtrar los datos por número de unidad si se proporciona
    if num_unidad is not None:
        # Asegurarse de que el número de unidad esté dentro de los límites permitidos
        if not (1 <= int(num_unidad[1:]) <= rango_filas[1] - rango_filas[0] + 1):
            print(f"Número de unidad inválido para el tipo {tipo_unidad}.")
            return

        # Determinar la fila correspondiente al número de unidad
        fila_unidad = rango_filas[0] + int(num_unidad[1:]) - 1

        # Obtener los valores de Programadas, Promedio y Ejecutadas para la unidad seleccionada
        programadas = data.iloc[fila_unidad, 2]  # Programadas
        promedio = data.iloc[fila_unidad, 5]     # Promedio
        ejecutadas = data.iloc[fila_unidad, 8]   # Ejecutadas

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
    else:
        print("Número de unidad no proporcionado.")
