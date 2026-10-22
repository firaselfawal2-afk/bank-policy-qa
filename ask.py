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

    for model_name in ["gemini-3.1-flash-lite", "gemini-3-flash-preview"]:
        try:
            response = gemini.models.generate_content(model=model_name, contents=prompt)
            return response.text
        except Exception as error:
            print(f"{model_name} failed: {error}")

    return "Sorry, the AI service is busy right now. Please try again later."



