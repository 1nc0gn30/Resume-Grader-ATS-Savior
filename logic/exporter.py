from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf(name, content):
    os.makedirs("data/reports", exist_ok=True)  # Ensure folder exists

    safe_name = name.replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/reports/{safe_name}_{timestamp}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in content.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename
