import os
from dotenv import load_dotenv
from google import genai
import numpy as np
from eval_data import test_cases

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Same knowledge base as rag.py (keep in sync)
documents = [
    "MongoDB is a NoSQL database that stores data in flexible, JSON-like documents.",
    "FastAPI is a modern Python web framework for building APIs quickly.",
    "MQTT is a lightweight messaging protocol often used for IoT devices.",
    "Python virtual environments isolate a project's dependencies from other projects.",
    "Git is a version control system that tracks changes in source code.",
    "An API key is a secret token used to authenticate requests to a service.",
]

def similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Embed all documents once
print("Embedding documents...")
doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)
doc_vectors = [e.values for e in doc_result.embeddings]

# Return the INDEXES of the top_k documents for a query
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
    return [idx for score, idx in scores[:top_k]]

# --- Measure Recall@k ---
def measure_recall(k):
    hits = 0
    for case in test_cases:
        top_indexes = retrieve_indexes(case["question"], top_k=k)
        if case["correct_doc"] in top_indexes:
            hits += 1
        else:
            # Print the failures so we can learn from them
            print(f"  MISS (Recall@{k}): '{case['question']}'")
            print(f"        expected doc {case['correct_doc']}, got {top_indexes}")
    recall = hits / len(test_cases)
    return recall

print(f"\nRunning {len(test_cases)} test questions...\n")

for k in [1, 2, 3]:
    recall = measure_recall(k)
    print(f"\nRecall@{k}: {recall:.2f}  ({int(recall*len(test_cases))}/{len(test_cases)} correct)\n")