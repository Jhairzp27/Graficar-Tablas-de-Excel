import matplotlib.pyplot as plt
from Models.costo_mantenimiento import generar_grafico_costo_mantenimiento
from Models.faltantes import generar_grafico_faltantes_anual
from Models.faltantes_findes import generar_grafico_faltantes_findes_anual
from Models.combustible import generar_grafico_combustible
from Models.vueltas_lun_viern import generar_grafico_vueltas_semanal
from Models.vueltas_findes import generar_grafico_vueltas_findes
from Models.faltantes_vueltas import generar_grafico_faltantes_vueltas_semanal
from Models.faltantes_vueltas_findes import generar_grafico_faltantes_vueltas_findes
from Models.produccion_anual import generar_grafico_produccion_anual
from Models.produccion_vuelta import generar_grafico_produccion_vuelta
from Models.produccion_porcentajes import generar_grafico_produccion_porcentajes
from Models.perdidas_y_ganancias import generar_grafico_perdidas_ganancia

def generar_graficos(filepath, tipo_unidad, num_unidad):
    # Crear tres figuras separadas
    fig1, axs1 = plt.subplots(3, 2, figsize=(8, 10))  # Figura para las primeras 6 figuras
    fig2 = plt.figure(figsize=(10, 8))  # Figura para la ventana 2
    fig1.suptitle("ANÁLISIS DE RENDIMIENTO AÑO 2023", fontsize=20)
    fig2.suptitle("ANÁLISIS DE RENDIMIENTO AÑO 2023", fontsize=20)
    axs1 = axs1.flatten()
    fig1.subplots_adjust(left=0.125, bottom=0.038, right=0.9, top=0.895, wspace=0.298, hspace=0.343)

    # Llama a tus funciones para generar los gráficos para las primeras seis figuras
    generar_grafico_vueltas_semanal(filepath, tipo_unidad, num_unidad, axs1[0])
    generar_grafico_vueltas_findes(filepath, tipo_unidad, num_unidad, axs1[1])
    generar_grafico_faltantes_anual(filepath, tipo_unidad, num_unidad, axs1[2])
    generar_grafico_faltantes_findes_anual(filepath, tipo_unidad, num_unidad, axs1[3])
    generar_grafico_faltantes_vueltas_semanal(filepath, tipo_unidad, num_unidad, axs1[4])
    generar_grafico_faltantes_vueltas_findes(filepath, tipo_unidad, num_unidad, axs1[5])

    # Definir las dimensiones y ubicación de los subgráficos usando subplot2grid para la ventana 2
    ax1 = plt.subplot2grid((3, 2), (0, 0))
    ax2 = plt.subplot2grid((3, 2), (0, 1))
    ax3 = plt.subplot2grid((3, 2), (1, 0))
    ax4 = plt.subplot2grid((3, 2), (1, 1))
    ax5 = plt.subplot2grid((3, 2), (2, 0), colspan=2)

    # Llama a tus funciones para generar los gráficos en la ventana 2
    generar_grafico_costo_mantenimiento(filepath, tipo_unidad, num_unidad, ax1)
    generar_grafico_combustible(filepath, tipo_unidad, num_unidad, ax2)  # Llamada al nuevo gráfico
    generar_grafico_produccion_anual(filepath, tipo_unidad, num_unidad, ax3)
    generar_grafico_produccion_vuelta(filepath, tipo_unidad, num_unidad, ax4)
    generar_grafico_produccion_porcentajes(filepath, num_unidad, ax5)

    # Llama a tu función para generar el otro gráfico en la ventana 3
    generar_grafico_perdidas_ganancia(filepath, num_unidad)

    plt.tight_layout()
    plt.close()
