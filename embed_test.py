from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "What is the late payment fee?",
    "Charges for paying after the due date",
    "The card is delivered by a shipping company",
]

vectors = model.encode(sentences)

print(vectors.shape)
print(model.similarity(vectors[0], vectors[1]))
print(model.similarity(vectors[0], vectors[2]))