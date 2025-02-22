import openpyxl

def obtener_opciones_desde_excel(filepath, tipo_unidad):
    """
    Obtiene las opciones de unidades desde un archivo Excel dependiendo del tipo de unidad.
    :param filepath: Ruta al archivo Excel.
    :param tipo_unidad: Tipo de unidad ("Grandes" o "Micros").
    :return: Lista de opciones disponibles, formateadas como 'G01', 'G02', etc.
    """
    try:
        wb = openpyxl.load_workbook(filepath, data_only=True)
        hoja = wb["PlantillaVueltas"]
        opciones = []

        # Configurar rango y prefijo según el tipo de unidad
        if tipo_unidad == "Grandes":
            rango = range(5, 31)  # A5 a A30
            columna = 1  # Columna A
            prefijo = "G"
        elif tipo_unidad == "Micros":
            rango = range(5, 31)  # B5 a B30
            columna = 2  # Columna B
            prefijo = "M"
        else:
            print("Tipo de unidad no válido.")
            return []

        # Obtener las opciones desde el rango
        for idx, row in enumerate(rango, start=1):
            valor = hoja.cell(row=row, column=columna).value
            if valor:  # Si el valor existe, agregarlo con el prefijo
                opciones.append(f"{prefijo}{idx:02d}")

        wb.close()
        return opciones

    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
        return []
    except KeyError:
        print(f"Error: La hoja 'PlantillaVueltas' no existe en el archivo '{filepath}'.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return []
