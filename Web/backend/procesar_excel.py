import pandas as pd

def procesar_archivo(file_path):
    """Carga un archivo Excel y devuelve un DataFrame."""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error al procesar archivo: {e}")
        return None
