import os
from dotenv import load_dotenv
from google import genai

# Load the secret key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini using your key
client = genai.Client(api_key=api_key)

try:
    # Send a question to the AI and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain what an API is in two simple sentences."
    )
    # Print the AI's answer
    print(response.text)
except Exception as e:
    print("Something went wrong:")
    print(e)