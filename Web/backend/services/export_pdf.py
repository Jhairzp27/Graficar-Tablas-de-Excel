from fpdf import FPDF
import os

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)  # Asegurar que la carpeta existe

def generate_custom_pdf(title="Reporte de Gráfico", footer_text="© Graficador Excel", orientation="P"):
    file_path = os.path.join(EXPORT_DIR, "grafico.png")

    if not os.path.exists(file_path):
        return None

    pdf = FPDF(orientation, "mm", "A4")
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, title, ln=True, align="C")

    # Agregar gráfico con validación de existencia
    if os.path.exists(file_path):
        pdf.image(file_path, x=10, y=30, w=180)
    else:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, "Error: No se encontró la imagen del gráfico", ln=True, align="C")

    # Agregar pie de página
    pdf.set_y(-20)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, footer_text, ln=True, align="C")

    pdf_output = os.path.join(EXPORT_DIR, "grafico.pdf")
    pdf.output(pdf_output)

    return pdf_output
