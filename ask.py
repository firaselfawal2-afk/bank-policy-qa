import os
import chromadb
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer

load_dotenv()
gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = SentenceTransformer("BAAI/bge-small-en-v1.5")
collection = chromadb.PersistentClient(path="chroma_db").get_collection("bank_policies")


def ask(question):
    question_vector = model.encode([question]).tolist()
    results = collection.query(query_embeddings=question_vector, n_results=5)

    context = ""
    for text, label in zip(results["documents"][0], results["metadatas"][0]):
        context += f"[{label['source']}, page {label['page_number']}]\n{text}\n\n"

    prompt = f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".
Mention the source and page.

Context:
{context}

Question: {question}"""

    response = gemini.models.generate_content(model="gemini-3.1-flash-lite", contents=prompt)
    return response.text


print(ask("What is the price of an iPhone?"))
