import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_grafico_costo_mantenimiento(filepath, tipo_unidad, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    try:
        data = pd.read_excel(filepath, sheet_name='CostoMantenimiento')
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

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

    if num_unidad is None or not num_unidad.startswith('U'):
        print("Número de unidad no proporcionado o inválido.")
        return

    # Validar el número de unidad
    try:
        num_unidad_idx = int(num_unidad[1:])
        if not (1 <= num_unidad_idx <= rango_filas[1] - rango_filas[0] + 1):
            print(f"Número de unidad {num_unidad} inválido para el tipo {tipo_unidad}.")
            return
    except ValueError:
        print("Formato de número de unidad inválido. Debe empezar con 'U' seguido de un número.")
        return

    # Determinar la fila correspondiente al número de unidad
    fila_unidad = rango_filas[0] + num_unidad_idx - 1

    # Seleccionar los valores de las celdas necesarias
    try:
        provision = data.iloc[fila_unidad, columna_provision_mec]
        promedio = data.iloc[fila_unidad, columna_promedio_mec]
        costo_real = data.iloc[fila_unidad, columna_costo_real_mec]
    except IndexError:
        print(f"Error al acceder a los datos de la unidad {num_unidad}. Verifique el rango de filas.")
        return

    # Crear el gráfico
    if ax is None:
        fig, ax = plt.subplots()

    categorias = ['Costo Provisión', 'Costo Promedio', 'Costo Real']
    valores = [provision, promedio, costo_real]
    colores = ['#87d349', '#FFA500', '#f9e826']
    width = 0.28

    ax.bar(categorias, valores, color=colores, width=width)

    for i, valor in enumerate(valores):
        valor_formateado = '{:,.2f}'.format(valor).replace(',', 'X').replace('.', ',').replace('X', '.') if pd.notna(valor) else '0.00'
        ax.text(i, valor, valor_formateado, ha='center', va='bottom')

    ax.set_ylim(0, max(valores) * 1.1 if any(pd.notna(valor) for valor in valores) else 1.0)
    ax.set_ylabel('Dólares [$]')
    ax.set_title(f'Costos Mantenimiento - Unidad {num_unidad} [$]')

    if ax is None:
        plt.show()
