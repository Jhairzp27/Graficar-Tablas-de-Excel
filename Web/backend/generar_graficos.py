import matplotlib.pyplot as plt
import pandas as pd
import os

UPLOAD_FOLDER = "backend/uploads"

def generar_grafico(columna):
    """Genera un gráfico de barras basado en la columna seleccionada."""
    file_path = os.path.join(UPLOAD_FOLDER, "datos.xlsx")
    df = pd.read_excel(file_path)
    
    if columna not in df.columns:
        return {"error": "Columna no encontrada"}

    plt.figure(figsize=(8, 4))
    df[columna].value_counts().plot(kind='bar', color='skyblue')
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.title(f"Distribución de {columna}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    img_path = os.path.join(UPLOAD_FOLDER, "grafico.png")
    plt.savefig(img_path)
    plt.close()
    
    return img_path
