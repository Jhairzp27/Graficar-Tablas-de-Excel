import matplotlib.pyplot as plt

# Funciones de generación de gráficos
from Models.costo_mantenimiento import generar_grafico_costo_mantenimiento
from Models.faltantes import generar_grafico_faltantes_anual
from Models.faltantes_findes import generar_grafico_faltantes_findes_anual
from Models.combustible import generar_grafico_combustible
from Models.vueltas_lun_viern import generar_grafico_vueltas_semanal
from Models.vueltas_findes import generar_grafico_vueltas_findes
# from Models.faltantes_vueltas import generar_grafico_faltantes_vueltas_semanal

def generar_graficos(filepath, tipo_unidad, num_unidad):
    """
    Genera gráficos basados en el tipo de unidad y el número de unidad seleccionados.
    :param filepath: Ruta al archivo Excel.
    :param tipo_unidad: Tipo de unidad ("Grandes" o "Micros").
    :param num_unidad: Número de la unidad seleccionada.
    """
    try:
        if tipo_unidad == "Grandes":
            generar_grafico_costo_mantenimiento(filepath, num_unidad)
            generar_grafico_combustible(filepath, num_unidad)
            generar_grafico_vueltas_semanal(filepath, num_unidad)
        elif tipo_unidad == "Micros":
            generar_grafico_faltantes_anual(filepath, num_unidad)
            generar_grafico_faltantes_findes_anual(filepath, num_unidad)
            generar_grafico_vueltas_findes(filepath, num_unidad)
        else:
            print("Tipo de unidad no reconocido.")
            return

        # Mostrar todos los gráficos generados
        plt.show()
    except Exception as e:
        print(f"Error al generar gráficos: {e}")
