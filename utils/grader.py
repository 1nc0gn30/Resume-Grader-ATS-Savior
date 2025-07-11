import fitz  # pymupdf
import re
from utils.db import store_report
from logic.ollama_client import send_to_ollama
from logic.exporter import generate_pdf
from logic.grader import sanitize_text  # optional - sanitize resume

def process_submission(name, email, preset, pdf_bytes):
    doc = fitz.open("pdf", pdf_bytes)
    text = "\n".join(page.get_text() for page in doc)
    clean_text = sanitize_text(text)
    result = send_to_ollama(clean_text, preset)
    score = extract_score(result)

    pdf_path = generate_pdf(name, result)
    store_report(name, email, preset, score, result, pdf_path)

    return result

def extract_score(text):
    match = re.search(r"Score: ?(\d{1,3})", text)
    return int(match.group(1)) if match else None
