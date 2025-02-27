from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
import os
from services.export_pdf import generate_custom_pdf

router = APIRouter(prefix="/export", tags=["Export"])

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

@router.get("/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(EXPORT_DIR, filename)
    
    if not os.path.exists(file_path):
        return {"error": "Archivo no encontrado"}

    file_extension = filename.split(".")[-1].lower()
    media_type = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "pdf": "application/pdf"
    }.get(file_extension, "application/octet-stream")

    return FileResponse(file_path, media_type=media_type, filename=filename)

@router.get("/pdf/")
async def download_custom_pdf(
    title: str = Query("Reporte de Gráfico"),
    footer_text: str = Query("© Graficador Excel"),
    orientation: str = Query("P")
):
    pdf_file = generate_custom_pdf(title, footer_text, orientation)

    if pdf_file is None:
        return {"error": "No hay gráficos disponibles para exportar"}

    return FileResponse(pdf_file, media_type="application/pdf", filename="grafico_personalizado.pdf")
