import fitz  # PyMuPDF
import os
from utils.db import store_report
from logic.ollama_client import send_to_ollama
from logic.exporter import generate_pdf


def sanitize_text(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").split())


def extract_score(text: str) -> int:
    import re
    match = re.search(r"Score: ?(\d{1,3})", text)
    return int(match.group(1)) if match else None


def process_submission(name, email, preset, pdf_bytes):
    # 1. Extract text from PDF
    try:
        doc = fitz.open("pdf", pdf_bytes)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
    except Exception as e:
        return f"Error reading PDF: {e}"

    # 2. Clean resume text
    clean_text = sanitize_text(text)

    # 3. Send to Ollama
    result = send_to_ollama(clean_text, preset)

    # 4. Extract score
    score = extract_score(result)

    # 5. Export to PDF (report)
    export_path = generate_pdf(name, email, preset, score, result)

    # 6. Store to DB
    store_report(name, email, preset, score, result, export_path)

    # 7. Return full result text
    return result
