import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "Give me a name for a new IoT monitoring startup."
temp = 1.5

# Try up to 3 times, in case the server is busy (503)
for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(temperature=temp),
            contents=prompt
        )
        print(f"Temperature {temp}:")
        print(response.text)
        break  # success — stop retrying
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        if attempt < 2:
            print("Waiting 5 seconds before retrying...")
            time.sleep(5)
        else:
            print("All attempts failed. Try again in a minute.")