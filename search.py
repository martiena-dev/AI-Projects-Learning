import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --- Our small "knowledge base" of documents ---
documents = [
    "MongoDB is a NoSQL database that stores data in flexible, JSON-like documents.",
    "FastAPI is a modern Python web framework for building APIs quickly.",
    "MQTT is a lightweight messaging protocol often used for IoT devices.",
    "Python virtual environments isolate a project's dependencies from other projects.",
    "Git is a version control system that tracks changes in source code.",
    "An API key is a secret token used to authenticate requests to a service.",
]

# --- Helper: measure similarity between two vectors ---
def similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# --- Step 1: Embed all documents once, up front ---
print("Embedding documents...")
doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)
doc_vectors = [e.values for e in doc_result.embeddings]
print("Done. Ready to search.\n")

# --- Step 2: The search function ---
def search(query, top_k=2):
    # Embed the question
    query_result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    query_vector = query_result.embeddings[0].values

    # Score every document against the question
    scores = []
    for i in range(len(documents)):
        score = similarity(query_vector, doc_vectors[i])
        scores.append((score, documents[i]))

    # Sort by score, highest first, return the top_k
    scores.sort(reverse=True)
    return scores[:top_k]

# --- Step 3: Try it! ---
#question = "How do I keep my project's Python packages separate?"
#question = "What tool tracks changes to my code?"
#question = "How do IoT devices send messages?"
#question = "What framework builds APIs fast in Python?"
question = "How do I prove who I am to an external service?"

print(f"Question: {question}\n")

results = search(question)
print("Top matches:")
for score, doc in results:
    print(f"  [{score:.3f}] {doc}")