import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --- Our knowledge base ---
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

# --- Embed all documents up front ---
print("Embedding documents...")
doc_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documents
)
doc_vectors = [e.values for e in doc_result.embeddings]
print("Ready.\n")

# --- RETRIEVE: find the most relevant documents ---
def retrieve(query, top_k=2):
    query_result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    query_vector = query_result.embeddings[0].values

    scores = []
    for i in range(len(documents)):
        score = similarity(query_vector, doc_vectors[i])
        scores.append((score, documents[i]))

    scores.sort(reverse=True)
    return [doc for score, doc in scores[:top_k]]

# --- GENERATE: answer using the retrieved documents ---
def answer(query):
    # Step 1: retrieve relevant docs
    relevant_docs = retrieve(query)

    # Step 2: build a prompt that includes them as context
    context = "\n".join(relevant_docs)
    prompt = f"""Use ONLY the context below to answer the question.
If the context doesn't contain the answer, say "I don't have information about that."

Context:
{context}

Question: {query}

Answer:"""

    # Step 3: send to the LLM
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text, relevant_docs

# --- Try it! ---
#question = "How do I keep my project's Python packages separate?"
#question = "What is the capital of France?"
#question = "What database stores JSON-like documents?"
question = "How do IoT devices communicate?"

result, sources = answer(question)

print(f"Question: {question}\n")
print("Retrieved these documents as context:")
for doc in sources:
    print(f"  - {doc}")
print(f"\nAnswer:\n{result}")