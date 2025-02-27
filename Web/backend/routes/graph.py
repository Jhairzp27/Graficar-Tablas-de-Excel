from fastapi import APIRouter, HTTPException
import pandas as pd
import matplotlib.pyplot as plt
import os
import io
import base64
from models.graph_config import GraphConfig

router = APIRouter(prefix="/graph", tags=["Graph"])

UPLOAD_DIR = "uploads"
EXPORT_DIR = "exports"

# Asegurar que las carpetas existan
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

@router.post("/")
async def generate_graph(config: GraphConfig):
    try:
        # Verificar si hay archivos subidos
        file_list = os.listdir(UPLOAD_DIR)
        if not file_list:
            raise HTTPException(status_code=400, detail="No hay archivos subidos")

        # Obtener el archivo más reciente
        file_path = os.path.join(UPLOAD_DIR, file_list[0])
        df = pd.read_excel(file_path)

        # 🔹 Verificar si las columnas existen en el archivo
        missing_columns = [col for col in [config.x_column, config.y_column] if col not in df.columns]
        if missing_columns:
            available_columns = ", ".join(df.columns)
            raise HTTPException(
                status_code=400,
                detail=f"Las siguientes columnas no existen en el archivo: {', '.join(missing_columns)}. "
                       f"Las columnas disponibles son: {available_columns}"
            )

        # Crear la figura antes de graficar
        fig, ax = plt.subplots(figsize=(8, 5))

        if config.graph_type == "barras":
            df.plot(kind="bar", x=config.x_column, y=config.y_column, ax=ax, color=config.colors or "blue")

        elif config.graph_type == "líneas":
            df.plot(kind="line", x=config.x_column, y=config.y_column, ax=ax, color=config.colors or "red")

        elif config.graph_type == "pastel":
            if df[config.y_column].isnull().any():
                raise HTTPException(status_code=400, detail="No se pueden graficar valores NaN en un gráfico de pastel")

            if (df[config.y_column] < 0).any():
                raise HTTPException(status_code=400, detail="No se pueden graficar valores negativos en un gráfico de pastel")

            df[config.y_column] = pd.to_numeric(df[config.y_column], errors="coerce")
            df_pie = df.groupby(config.x_column)[config.y_column].sum()

            colors = config.colors if config.colors and len(config.colors) > 0 else ["#FF9999", "#66B3FF", "#99FF99", "#FFD700"]
            df_pie.plot(kind="pie", autopct='%1.1f%%', colors=colors, startangle=90, ax=ax)

        elif config.graph_type == "dispersión":
            df[config.x_column] = pd.to_numeric(df[config.x_column], errors="coerce")
            df[config.y_column] = pd.to_numeric(df[config.y_column], errors="coerce")

            if df[config.x_column].isnull().any() or df[config.y_column].isnull().any():
                raise HTTPException(status_code=400, detail="Las columnas seleccionadas deben contener solo valores numéricos para gráficos de dispersión")

            # 🔹 Manejar colores para dispersión
            if config.colors and len(config.colors) == len(df):
                color = config.colors
            else:
                color = config.colors[0] if config.colors and len(config.colors) > 0 else "blue"

            # Convertir lista de colores en mapa de colores si es necesario
            if isinstance(color, list) and all(isinstance(c, str) for c in color):
                color = range(len(df))

            # Graficar dispersión
            scatter = ax.scatter(df[config.x_column], df[config.y_column], c=color, cmap="viridis", alpha=0.7, edgecolors="k")

            # Agregar barra de colores si se usa un mapa de colores
            if isinstance(color, range):
                plt.colorbar(scatter, ax=ax, label="Intensidad de color")

        else:
            raise HTTPException(status_code=400, detail="Tipo de gráfico no válido")

        ax.set_title(config.title, fontsize=config.font_size)
        ax.set_xlabel(config.x_label)
        ax.set_ylabel(config.y_label)
        
        if config.show_legend:
            ax.legend()

        # 🔹 Guardar correctamente antes de cerrar
        output_path = os.path.join(EXPORT_DIR, "grafico.png")
        fig.savefig(output_path, format="png", dpi=300, bbox_inches="tight")
        plt.close(fig)  # Cerrar la figura para liberar memoria

        # 🔹 Verificar que la imagen se guardó correctamente
        if not os.path.exists(output_path):
            print("❌ Error: La imagen no se guardó en exports/")
            raise HTTPException(status_code=500, detail="Error al guardar la imagen del gráfico.")
        else:
            print("✅ Imagen generada correctamente:", output_path)

        # 🔹 Convertir gráfico a base64 para enviarlo al frontend
        try:
            with open(output_path, "rb") as image_file:
                img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        
            if not img_base64:
                print("❌ Error: La imagen en base64 está vacía.")
                raise HTTPException(status_code=500, detail="Error al convertir la imagen a base64.")
        
            print("✅ Imagen convertida correctamente a base64:", img_base64[:50], "...")
        
        except Exception as e:
            print("❌ Error al convertir a base64:", str(e))
            raise HTTPException(status_code=500, detail=f"Error al convertir la imagen a base64: {str(e)}")
        
        # 🔹 Devolver la imagen en base64 al frontend
        return {"graph": img_base64, "filename": "grafico.png"}

    except Exception as e:
        print("❌ Error inesperado:", str(e))
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")
