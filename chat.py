import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create a chat session — it automatically remembers history for us
chat = client.chats.create(model="gemini-2.5-flash")

print("Chat started! Type 'quit' to exit.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        print("Goodbye!")
        break

    response = chat.send_message(user_message)
    print("AI:", response.text)
    print()