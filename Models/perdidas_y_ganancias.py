import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import locale

matplotlib.use('TkAgg')

def generar_grafico_perdidas_ganancia(filepath, num_unidad, ax= None):
    # Leer los datos desde el archivo Excel
    data = pd.read_excel(filepath, sheet_name='PerdidasYGanancias', header=None)
    # Eliminar filas con valores NaN
    data = data.dropna()
    # Obtener el tipo de unidad
    tipo_unidad = num_unidad[0]  # Obtener el primer dígito del número de unidad
    # Filtrar los datos por el tipo de unidad
    data_filtered = data[data[0].str.startswith(tipo_unidad)]
    # Obtener los valores de las unidades y sus respectivas pérdidas o ganancias
    unidades = data_filtered[0].str.split().str[0]  # Obtener solo el tipo de unidad
    valores = data_filtered[1]
    # Crear colores para las barras
    colores = ['#f9e826' if unidad == num_unidad else ('lightgreen' if valor >= 0 else 'lightcoral') for unidad, valor in zip(unidades, valores)]
    
    # Configuración local para el formato de números
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Usar el eje para graficar
    ax.bar(unidades.index, valores, color=colores)
    
    # Etiquetar la barra del tipo de unidad especificado
    for i, valor in enumerate(valores):
        if unidades.iloc[i] == num_unidad:
            # Ajustar el formato de la etiqueta para mostrar solo dos decimales
            etiqueta = locale.format_string("%.2f", valor, grouping=True)
            # Calcular la posición central de la barra para ubicar la etiqueta
            posicion_etiqueta = unidades.index[i] + 0.2
            # Ajustar la posición vertical de la etiqueta y agregar un pequeño desplazamiento hacia arriba
            ax.text(posicion_etiqueta, valor, etiqueta, ha='center', va='bottom', fontsize=8, color='black', weight='bold')
    
    ax.set_title(f'Pérdidas y Ganancias - Unidad {num_unidad}')
    
    # Colocar los nombres de las unidades en el eje x de forma vertical
    ax.set_xticks(unidades.index)
    ax.set_xticklabels(unidades, rotation='vertical')
    
    # Dividir el eje y en tres partes y colorearlas
    ax.set_ylabel('Pérdidas' + ' '*20 +'Dólares [$]' + ' '*20 + 'Ganancias')
    ax.yaxis.set_label_coords(-0.06, 0.5)  # Ajustar la posición del eje y
    
    # Cambiar el color de la línea del eje x
    ax.axhline(0, color='black', linewidth=0.5)  # Cambiado a negro para mejorar la visibilidad
    
    # Agregar título a la página
    fig.suptitle('ANÁLISIS DE RENDIMIENTO AÑO 2023', fontsize=20)
    
    plt.tight_layout()
    plt.show()
    plt.close()

# Establecer la configuración local para que los números se formateen correctamente
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')