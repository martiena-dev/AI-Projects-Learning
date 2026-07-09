import os
from dotenv import load_dotenv
from google import genai
import numpy as np
from knowledge_base import documents

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# A HARDER knowledge base: many docs are similar to each other (overlapping topics)
# documents = [
#     # Multiple database docs (similar to each other = harder to tell apart)
#     "MongoDB is a NoSQL database that stores data in flexible, JSON-like documents.",
#     "PostgreSQL is a relational database that uses tables and SQL queries.",
#     "Redis is an in-memory database often used for caching and fast lookups.",
#     "SQLite is a lightweight file-based database good for small applications.",
#     # Multiple Python/web docs
#     "FastAPI is a modern Python web framework for building APIs quickly.",
#     "Flask is a lightweight Python web framework that is simple and flexible.",
#     "Django is a full-featured Python web framework with built-in admin and ORM.",
#     # Multiple messaging/protocol docs
#     "MQTT is a lightweight messaging protocol often used for IoT devices.",
#     "HTTP is the protocol used for communication between web browsers and servers.",
#     "WebSocket is a protocol that enables real-time two-way communication.",
#     # Environment / tooling
#     "Python virtual environments isolate a project's dependencies from other projects.",
#     "Docker containers package an application with all its dependencies to run anywhere.",
#     "Git is a version control system that tracks changes in source code.",
# ]

def similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Embedding documents...")
doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)
doc_vectors = [e.values for e in doc_result.embeddings]
print("Ready.\n")

def retrieve_indexes(query, top_k):
    query_result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    query_vector = query_result.embeddings[0].values
    scores = []
    for i in range(len(documents)):
        score = similarity(query_vector, doc_vectors[i])
        scores.append((score, i))
    scores.sort(reverse=True)
    return [(idx, score) for score, idx in scores[:top_k]]

# Quick manual test — try a deliberately ambiguous question
#question = "What database should I use for caching?"
#question = "Which Python framework is simplest?"
question = "What protocol allows real-time communication?"

print(f"Question: {question}\n")
results = retrieve_indexes(question, top_k=3)
for idx, score in results:
    print(f"  [{score:.3f}] doc {idx}: {documents[idx]}")