from read_pdf import load_pages
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)


def make_chunks():
    chunks = []
    for page in load_pages():
        for piece in splitter.split_text(page["text"]):
            chunks.append({
                "source": page["source"],
                "page_number": page["page_number"],
                "text": piece,
            })
    return chunks


chunks = make_chunks()
print(len(chunks), "chunks")
print(chunks[10])