from fastapi import FastAPI, UploadFile, File
import pandas as pd
import shutil
import os
from backend.procesar_excel import procesar_archivo
from backend.generar_graficos import generar_grafico
from backend.generar_pdf import generar_pdf

app = FastAPI()

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "API del Graficador de Excel funcionando correctamente"}

@app.post("/upload-excel/")
async def upload_excel(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    df = procesar_archivo(file_path)
    return {"message": "Archivo procesado", "columns": df.columns.tolist()}

@app.get("/generar-grafico/")
def generar_grafico_endpoint(columna: str):
    ruta_imagen = generar_grafico(columna)
    return {"message": "Gráfico generado", "image_path": ruta_imagen}

@app.get("/generar-pdf/")
def generar_pdf_endpoint():
    ruta_pdf = generar_pdf()
    return {"message": "Reporte PDF generado", "pdf_path": ruta_pdf}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
