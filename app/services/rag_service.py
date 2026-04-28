import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Free model (works well enough)
HF_MODEL = "google/flan-t5-base"

API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_answer(context_chunks, question):
    try:
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are an AI assistant. Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.3,
                "return_full_text": False
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"HF API Error: {response.text}")

        result = response.json()

        # HF response format
        if isinstance(result, list):
            return result[0].get("generated_text", "").strip()
        else:
            return str(result)

    except Exception as e:
        raise Exception(f"Error generating answer: {str(e)}")