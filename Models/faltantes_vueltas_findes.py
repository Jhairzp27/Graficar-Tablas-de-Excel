import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_grafico_faltantes_vueltas_findes(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='Faltantes')
    rango_filas = None
    columna_faltante_anual = None
    columna_faltante_real_anual = None

    # Determinar los rangos de filas y columnas para unidades Grandes y Micros
    if tipo_unidad == "Grandes":
        rango_filas = (72, 98)
        columna_faltante_anual = 3  # Columna D
        columna_faltante_real_anual = 4   # Columna E
        ylabel = "Número de Vueltas"
        title = f'Faltantes S-D - Unidad {num_unidad}'
    elif tipo_unidad == "Micros":
        rango_filas = (98, 135)
        columna_faltante_anual = 3  # Columna D
        columna_faltante_real_anual = 4   # Columna E
        title = f'Faltantes S-D - Unidad {num_unidad} [Km]'
        ylabel = "Kilómetros Recorridos [Km]"
    else:
        print("Tipo de unidad no válido.")
        return

    # Filtrar los datos por número de unidad si se proporciona
    if num_unidad is not None:
        # Determinar la fila correspondiente al número de unidad
        fila_unidad = rango_filas[0] + int(num_unidad[1:]) - 1
        # Seleccionar los valores de las celdas necesarias
        provision = data.iloc[fila_unidad, columna_faltante_anual]
        promedio = data.iloc[fila_unidad, columna_faltante_real_anual]

        # Reemplazar NaN con ceros
        provision = provision if pd.notna(provision) else 0
        promedio = promedio if pd.notna(promedio) else 0

        # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
        if ax is None:
            ax = plt.subplots()  # Tamaño de la figura ajustable
        else:
            ax.clear()

        # Configurar las categorías, valores y colores de las barras
        categorias = ['Promedio/Vueltas', 'Real/Vueltas']
        valores = [provision, promedio]
        custom_colors = ['#FFA500', '#f9e826']

        # Ajustar el ancho de la barra
        bar_width = 0.19  # Ancho de las barras

        # Definir manualmente las posiciones de las barras
        positions = np.arange(len(categorias))

        ax.bar(positions, valores, color=custom_colors, width=bar_width)
        ax.invert_yaxis()

        # Agregar etiquetas de valores a las barras con un pequeño desplazamiento vertical
        for i, valor in enumerate(valores):
            valor_formateado = '{:,.2f}'.format(valor).replace(',', 'X').replace('.', ',').replace('X', '.')
            ax.text(positions[i], valor, valor_formateado, ha='center', va='bottom', fontsize=10, color='black')

        ax.set_xticks(positions)  # Posiciones de las etiquetas
        ax.set_xticklabels(categorias)  # Etiquetas de las categorías
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        # Ajustar el margen en el eje y para evitar que las etiquetas se superpongan con el borde del gráfico
        ax.margins(y=0.1)

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
