import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico_faltantes_findes_anual(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='Faltantes')
    rango_filas = None
    columna_faltante_anual = None
    columna_faltante_real_anual = None

    # Determinar los rangos de filas y columnas para unidades Grandes y Micros
    if tipo_unidad == "Grandes":
        rango_filas = (74, 99)
        columna_faltante_anual = 1  # Columna B
        columna_faltante_real_anual = 2   # Columna C
    elif tipo_unidad == "Micros":
        rango_filas = (100, 137)
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
        categorias = ['Promedio S-D', 'Real S-D']
        valores = [provision, promedio]
        custom_colors = ['#FFA500', '#f9e826']

        width = 0.6  # Ajusta el ancho de las barras
        ax.bar(categorias, valores, width=width, color=custom_colors)
        ax.invert_yaxis()
        
        # Agregar etiquetas de valores a las barras
        for i, valor in enumerate(valores):
            ax.text(i, valor, str(round(valor, 2)), ha='center', va='bottom')

        ax.set_ylabel('Dólares [$]')
        ax.set_title(f'Faltantes S-D - Unidad {num_unidad}')

        # Añadir un margen en el límite superior del eje y
        ylim = ax.get_ylim()
        ax.set_ylim(ylim[0], ylim[1] * 1.05)  # Ajusta el margen según tu preferencia

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
