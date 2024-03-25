import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico_combustible(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    custom_colors = ['#f9e826','#FFA500','#a3c4d0']
    data = pd.read_excel(filepath, sheet_name='Diesel')
    rango_filas = None
    columna_consumo_real = None
    columna_promedio_km_galon = None
    columna_km_galon = None

    # Determinar los rangos de filas y columnas para unidades Grandes y Micros
    if tipo_unidad == "Grandes":
        rango_filas = (3, 29)
        columna_consumo_real = 2  # Columna B
        columna_promedio_km_galon = 3   # Columna C
        columna_km_galon = 4 #Columna D
    elif tipo_unidad == "Micros":
        rango_filas = (29, 63)
        columna_consumo_real = 2  # Columna B
        columna_promedio_km_galon = 3   # Columna C
        columna_km_galon = 4 #Columna D
    else:
        print("Tipo de unidad no válido.")
        return

    # Filtrar los datos por número de unidad si se proporciona
    if num_unidad is not None:
        # Convertir num_unidad a cadena si no lo es
        num_unidad = str(num_unidad)

        # Determinar la fila correspondiente al número de unidad
        fila_unidad = rango_filas[0] + int(num_unidad[1:]) - 1
        # Seleccionar los valores de las celdas necesarias
        real = data.iloc[fila_unidad, columna_consumo_real]
        promedio_km_galon = data.iloc[fila_unidad, columna_promedio_km_galon]
        km_galon = data.iloc[fila_unidad, columna_km_galon]

        # Reemplazar NaN con ceros
        real = real if pd.notna(real) else 0
        promedio_km_galon = promedio_km_galon if pd.notna(promedio_km_galon) else 0

        # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
        if ax is None:
            ax = plt.subplots()
        else:
            ax.clear()

        # Configurar las categorías, valores y colores de las barras
        categorias = ['Real', 'Promedio Km/Galón',  'Km/Galón']
        valores = [real, promedio_km_galon, km_galon]
        width = 0.19

        ax.bar(categorias, valores, color=custom_colors, width=width)
        
        # Agregar etiquetas de valores a las barras
        for i, valor in enumerate(valores):
            valor_formateado = '{:,.2f}'.format(valor).replace(',', 'X').replace('.', ',').replace('X', '.')
            ax.text(i, valor, valor_formateado, ha='center', va='bottom')

        # Ajustar el límite inferior y superior del eje y automáticamente de manera más dinámica
        max_value = max(valores)
        min_value = min(valores)
        diff = max_value - min_value
        ylim_bottom = min_value - diff * 0.1  # Reducir el límite inferior un 10%
        ylim_top = max_value + diff * 0.1  # Añadir un margen del 10% al límite superior

        ax.set_ylabel('Dólares [$]')
        ax.set_title(f'Combustible - Unidad - {num_unidad} [$]')
        ax.set_ylim(max(ylim_bottom, 0), ylim_top)  # Establecer límite superior e inferior del eje y, asegurando que el límite inferior no sea negativo

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
