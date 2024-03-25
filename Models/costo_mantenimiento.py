import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_grafico_costo_mantenimiento(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='CostoMantenimiento')
    rango_filas = None
    columna_provision_mec = None
    columna_promedio_mec = None
    columna_costo_real_mec = None
    
    # Determinar los rangos de filas y columnas para unidades Grandes y Micros
    if tipo_unidad == "Grandes":
        rango_filas = (3, 29)
        columna_provision_mec = 1  # Columna B
        columna_promedio_mec = 2   # Columna C
        columna_costo_real_mec = 3 # Columna D
    elif tipo_unidad == "Micros":
        rango_filas = (29, 63)  # Ajuste del rango de filas
        columna_provision_mec = 1  # Columna B
        columna_promedio_mec = 2   # Columna C
        columna_costo_real_mec = 3 # Columna D
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
        # Seleccionar los valores de las celdas necesarias
        provision = data.iloc[fila_unidad, columna_provision_mec]
        promedio = data.iloc[fila_unidad, columna_promedio_mec]
        costo_real = data.iloc[fila_unidad, columna_costo_real_mec]

        # Crear el gráfico de barras en el eje proporcionado (o en uno nuevo si no se proporciona)
        if ax is None:
            ax = plt.subplots()
        else:
            ax.clear()

        # Configurar las categorías, valores y colores de las barras
        categorias = ['Costo Provisión', 'Costo Promedio', 'Costo Real']
        valores = [provision, promedio, costo_real]
        custom_colors = ['#87d349', '#FFA500', '#f9e826']
        width = 0.28

        ax.bar(categorias, valores, color=custom_colors, width=width)
        
        # Agregar etiquetas de valores a las barras
        for i, valor in enumerate(valores):
            if pd.notna(valor):
                valor_formateado = '{:,.2f}'.format(valor).replace(',', 'X').replace('.', ',').replace('X', '.')
            else:
                valor_formateado = '0.00'  # Si el valor es NaN, se muestra como 0.00
            ax.text(i, valor, valor_formateado, ha='center', va='bottom')

        # Ajustar el límite superior del eje y automáticamente con un margen
        ylim = max(valores) * 1.1 if any(pd.notna(valor) for valor in valores) else 1.0  # Ajustar límite superior con un 10% adicional si hay valores diferentes de NaN
        
        if np.isfinite(ylim):  # Verificar si ylim es un número finito
            ax.set_ylim(0, ylim)  # Establecer límite superior del eje y
        else:
            print("El límite superior del eje y no es un número finito.")

        ax.set_xticks(categorias)
        ax.set_ylabel('Dólares [$]')
        ax.set_title(f'Costos Mantenimiento - Unidad {num_unidad} [$]')

        if ax is None:
            plt.show()
            plt.close()
    else:
        print("Número de unidad no proporcionado.")
