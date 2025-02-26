from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

UPLOAD_FOLDER = "backend/uploads"

def generar_pdf():
    """Genera un reporte en PDF con el gráfico generado."""
    pdf_path = os.path.join(UPLOAD_FOLDER, "reporte.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "Reporte de Análisis de Datos")

    img_path = os.path.join(UPLOAD_FOLDER, "grafico.png")
    if os.path.exists(img_path):
        c.drawImage(img_path, 100, 500, width=300, height=200)

    c.save()
    return pdf_path
