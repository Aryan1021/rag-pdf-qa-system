import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_answer(context_chunks, question):
    try:
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a strict AI assistant.

STRICT RULES (must follow):
1. Answer ONLY from the given context
2. Output MUST follow the exact format below
3. Do NOT write paragraphs
4. Do NOT combine sentences
5. Keep everything short

FORMAT (STRICT):
Summary: <one short sentence>

- Point 1
- Point 2
- Point 3
- Point 4

Answer ONLY in the given format. No extra text.

If answer is not found, return:
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