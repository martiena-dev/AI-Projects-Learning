import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Turn a piece of text into an embedding (a list of numbers)
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="The cat sat on the mat."
)

embedding = result.embeddings[0].values

print("How many numbers in this embedding:", len(embedding))
print("First 10 numbers:", embedding[:10])