import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from your .env file")

client = genai.Client(api_key=api_key)

MODELS = ["gemini-3.8-flash", "gemini-3.6-flash"]
RETRIES = 3

SYSTEM_PROMPT = (
    "You are Friday, a helpful voice assistant. "
    "Answer in 1-3 short sentences using plain text. "
    "Be friendly, clear, and concise."
)


def ask_ai(question):
    quota_exhausted = False
    service_busy = False

    for model in MODELS:
        for attempt in range(RETRIES):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=question,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    ),
                )

                return response.text or "Sorry, I could not generate an answer."

            except Exception as e:
                error = str(e).upper()

                # Quota limit: try another model, without retrying this one
                if "429" in error or "RESOURCE_EXHAUSTED" in error:
                    print(f"Friday: Request limit reached for {model}.")
                    quota_exhausted = True
                    break

                # Temporary server problem: retry a few times
                if "503" in error or "UNAVAILABLE" in error:
                    service_busy = True
                    print(f"Friday: Temporary issue. Retrying ({attempt + 1}/{RETRIES})...")

                    if attempt < RETRIES - 1:
                        time.sleep(2 * (attempt + 1))
                    continue

                # Other errors
                print(f"Friday: Could not use {model}.")
                break

    if quota_exhausted:
        return (
            "Sorry, my AI request limit has been reached. "
            "Please try again later."
        )

    if service_busy:
        return "Sorry, the AI service is temporarily unavailable. Please try again."

    return "Sorry, I could not get an answer. Please check your API settings."


if __name__ == "__main__":
    question = input("Ask Friday: ")
    print("Friday:", ask_ai(question))
