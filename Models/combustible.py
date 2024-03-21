import pandas as pd
import matplotlib.pyplot as plt


def generar_grafico_combustible(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    custom_colors = ['#FFA500', '#f9e826']
    data = pd.read_excel(filepath, sheet_name='Diesel')
    rango_filas = None
    columna_faltante_anual = None
    columna_faltante_real_anual = None

    # Determinar los rangos de filas y columnas para unidades Grandes y Micros
    if tipo_unidad == "Grandes":
        rango_filas = (5, 30)
        columna_faltante_anual = 1  # Columna B
        columna_faltante_real_anual = 2   # Columna C
    elif tipo_unidad == "Micros":
        rango_filas = (31, 65)
        columna_faltante_anual = 1  # Columna B
        columna_faltante_real_anual = 2   # Columna C
    else:
        print("Tipo de unidad no válido.")
        return

    # Filtrar los datos por número de unidad si se proporciona
    if num_unidad is not None:
        # Determinar la fila correspondiente al número de unidad
        fila_unidad = rango_filas[0] + int(num_unidad[1:]) - 1
        # Seleccionar los valores de las celdas necesarias
        provision = data.iloc[fila_unidad, columna_faltante_anual]
        promedio = data.iloc[fila_unidad - 2, columna_faltante_real_anual]

        # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
        if ax is None:
            ax = plt.subplots()
        else:
            ax.clear()

        # Configurar las categorías, valores y colores de las barras
        categorias = ['Promedio', 'Real']
        valores = [provision, promedio]
        width = 0.15

        ax.bar(categorias, valores, color=custom_colors, width=width)
        
        # Agregar etiquetas de valores a las barras
        for i, valor in enumerate(valores):
            valor_formateado = '{:,.2f}'.format(valor).replace(',', 'X').replace('.', ',').replace('X', '.')
            ax.text(i, valor, valor_formateado, ha='center', va='bottom')

        # Ajustar el límite superior del eje y automáticamente
        max_value = max(valores)
        ylim = max_value + max_value * 0.1  # Añadir un margen del 10% al límite superior

        ax.set_ylabel('Dólares [$]')
        ax.set_title(f'Combustible - Unidad - {num_unidad}')
        ax.set_ylim(0, ylim)  # Establecer límite superior del eje y

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
