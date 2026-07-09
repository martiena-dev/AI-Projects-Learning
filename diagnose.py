import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

documents = [
    "MongoDB is a NoSQL database that stores data in flexible, JSON-like documents.",
    "PostgreSQL is a relational database that uses tables and SQL queries.",
    "Redis is an in-memory database often used for caching and fast lookups.",
    "SQLite is a lightweight file-based database good for small applications.",
    "FastAPI is a modern Python web framework for building APIs quickly.",
]

def similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Embed docs
doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)
doc_vectors = [e.values for e in doc_result.embeddings]

# Embed a query that CLEARLY should match Redis (doc 2)
query = "What in-memory store is used for caching?"
q_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)
q_vector = q_result.embeddings[0].values

print(f"Query: {query}\n")
print("Similarity to each document:")
for i, doc in enumerate(documents):
    score = similarity(q_vector, doc_vectors[i])
    print(f"  doc {i} [{score:.4f}]: {doc}")

# Also check: are all the doc vectors even different from each other?
print("\nAre document vectors distinct? (doc 0 vs each):")
for i in range(len(documents)):
    score = similarity(doc_vectors[0], doc_vectors[i])
    print(f"  doc 0 vs doc {i}: {score:.4f}")