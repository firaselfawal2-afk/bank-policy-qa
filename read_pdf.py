from pathlib import Path
from pypdf import PdfReader

def clean(text):
    return " ".join(text.split())
def load_pages():
    pages = []

    for pdf_path in Path("data").glob("*.pdf"):
        reader = PdfReader(pdf_path)
        for i, page in enumerate(reader.pages):
            text = clean(page.extract_text())
            if not text:
                continue
            pages.append({
                "source": pdf_path.name,
                "page_number": i + 1,
                "text": text,
            })
    return pages