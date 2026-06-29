import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# The system prompt: shapes HOW the model behaves
#system_instruction = "You are a senior Python code reviewer. You are concise, direct, and always point out security issues first."
#system_instruction = "You are a friendly teacher explaining to a complete beginner. Use simple analogies."
system_instruction = "You are a sarcastic senior engineer who has seen every bug. Be brutally honest but helpful."

# The user prompt: the actual task
user_prompt = "Review this code: password = '12345'; if user_input == password: print('access granted')"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction
    ),
    contents=user_prompt
)
print(response.text)