import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("bank_policies")

question = "How is the credit card delivered?"
question_vector = model.encode([question]).tolist()

results = collection.query(query_embeddings=question_vector, n_results=8)

for text, label in zip(results["documents"][0], results["metadatas"][0]):
    print(label["source"], "- page", label["page_number"])
    print(text[:300])
    print("---")