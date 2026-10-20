import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("bank_policies")

question = "Can i get a supplementary card?"
question_vector = model.encode([question]).tolist()

results = collection.query(query_embeddings=question_vector, n_results=3)

for text, label in zip(results["documents"][0], results["metadatas"][0]):
    print(label["source"], "- page", label["page_number"])
    print(text[:300])
    print("---")