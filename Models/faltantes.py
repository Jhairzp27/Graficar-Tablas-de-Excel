import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_grafico_faltantes_anual(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='Faltantes')
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
        promedio = data.iloc[fila_unidad-2, columna_faltante_real_anual]

        # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
        if ax is None:
            ax = plt.subplots()
        else:
            ax.clear()

        # Configurar las categorías, valores y colores de las barras
        categorias = ['Promedio L-V', 'Real L-V']
        valores = [provision, promedio]
        custom_colors = ['#FFA500', '#f9e826']

        # Ajustar el ancho de las barras y las posiciones de las barras
        width = 0.15  # Ancho de las barras
        positions = np.arange(len(categorias))  # Posiciones de las barras
        ax.bar(positions, valores, color=custom_colors, width=width)
        ax.invert_yaxis()
        # Agregar etiquetas de valores a las barras con un pequeño desplazamiento vertical
        for i, valor in enumerate(valores):
            # Verificar si el valor es finito y numérico antes de agregar el texto
            if np.isfinite(valor) and np.isreal(valor):
                ax.text(positions[i], valor, str(round(valor, 2)), ha='center', va='bottom', fontsize=10, color='black')

        ax.set_xticks(positions)
        ax.set_xticklabels(categorias)  # Etiquetas de las categorías
        ax.set_ylabel('Dólares [$]')
        ax.set_title(f'Faltantes L-V - Unidad {num_unidad}')

        # Ajustar el margen en el eje y para evitar que las etiquetas se superpongan con el borde del gráfico
        ax.margins(y=0.1)

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
