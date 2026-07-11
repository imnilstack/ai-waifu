import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

from src.config.config import config

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

AI_CONFIG = config["ai"]


def generate_response(prompt: str) -> str:
    for _ in range(3):
        try:
            response = client.models.generate_content(
                model=AI_CONFIG["model"],
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=AI_CONFIG["temperature"],
                    max_output_tokens=AI_CONFIG["max_tokens"],
                ),
            )
            return response.text or ""

        except ServerError:
            print("google servers busy, retrying...")
            time.sleep(2)

    return "sorry, google's servers are overloaded right now."
