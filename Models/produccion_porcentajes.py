from matplotlib import pyplot as plt
import matplotlib
import pandas as pd

matplotlib.use('TkAgg')

def generar_grafico_produccion_porcentajes(filepath, num_unidad, ax=None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='Producción', header=None)
    # Eliminar filas con valores NaN
    data = data.dropna()
    # Obtener el tipo de unidad
    tipo_unidad = num_unidad[0]  # Obtener el primer dígito del número de unidad
    # Filtrar los datos por el tipo de unidad
    data_filtered = data[data[0].str.startswith(tipo_unidad)]
    # Obtener los valores de las unidades y sus respectivos porcentajes de pérdidas o ganancias
    unidades = data_filtered[0].str.split().str[0]  # Obtener solo el tipo de unidad
    porcentajes = data_filtered[5] * 100  # Convertir el valor a porcentaje multiplicándolo por 100
    
    # Crear colores para las barras
    colores = ['#f9e826' if unidad == num_unidad else ('lightgreen' if porcentaje >= 0 else 'lightcoral') for unidad, porcentaje in zip(unidades, porcentajes)]
    
    # Graficar
    if ax is None:
        ax = plt.subplots()
    else:
        ax.clear()
    ax.bar(unidades.index, porcentajes, color=colores)
    
    # Etiquetar la barra del tipo de unidad especificado
    for i, porcentaje in enumerate(porcentajes):
        if unidades.iloc[i] == num_unidad:
            # Ajustar el formato de la etiqueta para mostrar el porcentaje con dos decimales y el símbolo de porcentaje
            etiqueta = f'{porcentaje:.2f}%'  # Muestra los valores con dos decimales y el símbolo de porcentaje
            # Calcular la posición central de la barra para ubicar la etiqueta
            posicion_etiqueta = unidades.index[i] + 0.2
            # Ajustar la posición vertical de la etiqueta y agregar un pequeño desplazamiento hacia arriba
            ax.text(posicion_etiqueta, porcentaje, etiqueta, ha='center', va='bottom', fontsize=8, color='black', weight='bold')
    ax.set_title(f'Producción Total Flota - Unidad {num_unidad} [%]')
    
    # Colocar los nombres de las unidades en el eje x de forma vertical
    ax.set_xticks(unidades.index)
    ax.set_xticklabels(unidades, rotation='vertical')
    ax.set_ylabel("Porcentaje [100%]")
    # Cambiar el color de la línea del eje x
    ax.axhline(0, color='black', linewidth=0.5)  # Cambiado a negro para mejorar la visibilidad
    
    plt.tight_layout()
    plt.show()
    plt.close()
