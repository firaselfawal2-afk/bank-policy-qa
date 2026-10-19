from pathlib import Path
from pypdf import PdfReader

def clean(text):
    return " ".join(text.split())

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
print(len(pages),"pages total")
print(pages[5])