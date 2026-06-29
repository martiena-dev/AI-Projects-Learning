import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Try different prompts — change this one line and re-run
#prompt = "Explain what a database is to a 10-year-old."
#prompt = "Write a haiku about Python programming."
#prompt = "List 3 reasons IoT devices fail. Be concise."
#prompt = "Translate 'Hello, how are you?' into Hindi, Tamil, and Telugu."
prompt = "Write a Python function that checks if a number is prime."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
print(response.text)