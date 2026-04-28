import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_answer(context_chunks, question):
    try:
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are an AI assistant. Answer ONLY using the given context.

If the answer is not in the context, say:
"I cannot find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama Error: {response.text}")

        result = response.json()

        return result.get("response", "").strip()

    except Exception as e:
        raise Exception(f"Error generating answer: {str(e)}")