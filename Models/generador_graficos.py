import matplotlib
import matplotlib.pyplot as plt

# Aquí importa tus funciones de generación de gráficos
from Models.costo_mantenimiento import generar_grafico_costo_mantenimiento
from Models.vueltas import generar_grafico_vueltas
from Models.faltantes import generar_grafico_faltantes_anual
from Models.faltantes_findes import generar_grafico_faltantes_findes_anual
from Models.combustible import generar_grafico_combustible
from Models.perdidas_y_ganancias import generar_grafico_perdidas_ganancia

matplotlib.use('TkAgg')  # Especificar el backend antes de importar pyplot

# Define tu función de generación de gráficos
def generar_graficos(filepath, tipo_unidad, num_unidad):
    if tipo_unidad == "Grandes" or tipo_unidad == "Micros":
        # Crear dos figuras separadas
        fig1, axs1 = plt.subplots(3, 2, figsize=(10, 8))  # Figura para las primeras 6 figuras
        fig2, ax7 = plt.subplots(figsize=(10, 6))  # Figura para la séptima figura

        fig1.suptitle("ANÁLISIS DE RENDIMIENTO", fontsize=20)
        fig2.suptitle("ANÁLISIS DE RENDIMIENTO", fontsize=20)

        axs1 = axs1.flatten()
        fig1.subplots_adjust(left=0.1, bottom=0.055, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
        
        # Llama a tus funciones para generar los gráficos para las primeras seis figuras
        generar_grafico_vueltas(filepath, tipo_unidad, num_unidad, axs1[0:2])
        generar_grafico_faltantes_anual(filepath, tipo_unidad, num_unidad, axs1[2])
        generar_grafico_faltantes_findes_anual(filepath, tipo_unidad, num_unidad, axs1[3])
        generar_grafico_costo_mantenimiento(filepath, tipo_unidad, num_unidad, axs1[4])
        generar_grafico_combustible(filepath, tipo_unidad, num_unidad, axs1[5])

        # Ajustar la escala de los ejes para las primeras seis figuras
        # for ax in axs1:
        #     ax.set_xticks(range(0, int(ax.get_xlim()[1]) + 1, 1000))
        #     ax.set_yticks(range(0, int(ax.get_ylim()[1]) + 1, 1000))

        # Llama a la función para generar el gráfico para la séptima figura
        generar_grafico_perdidas_ganancia(filepath, num_unidad, ax7)

        # Desactivar los ejes y el marco en la séptima figura
        ax7.axis('off')
        plt.close()

    else:
        print("Tipo de unidad no válido. Debe ser 'Grandes' o 'Micros'.")
