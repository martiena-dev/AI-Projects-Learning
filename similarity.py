import os
from dotenv import load_dotenv
from google import genai
import numpy as np

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# A helper that measures how similar two embeddings are (1.0 = identical meaning, 0 = unrelated)
def similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Embed several sentences
sentences = [
    "The cat sat on the mat.",
    "A feline rested on the rug.",
    "Quarterly revenue increased by 20 percent.",
    "The company's earnings grew significantly.",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=sentences
)
vectors = [e.values for e in result.embeddings]

# Compare sentence 0 (the cat) against all the others
print("Comparing: '" + sentences[0] + "'\n")
for i in range(len(sentences)):
    score = similarity(vectors[0], vectors[i])
    print(f"  vs '{sentences[i]}'")
    print(f"     similarity: {score:.3f}\n")