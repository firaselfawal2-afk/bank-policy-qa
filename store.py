import chromadb
from sentence_transformers import SentenceTransformer
from chunker import make_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("bank_policies")

chunks = make_chunks()
texts = [c["text"] for c in chunks]
vectors = model.encode(texts)

collection.upsert(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=texts,
    embeddings=vectors.tolist(),
    metadatas=[{"source": c["source"], "page_number": c["page_number"]} for c in chunks],
)

print(collection.count(), "chunks stored")