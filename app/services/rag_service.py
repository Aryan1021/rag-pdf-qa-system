import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_answer(context_chunks, question):
    try:
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a strict and precise AI assistant.

Rules:
- Answer ONLY using the given context
- Be VERY concise (max 4 bullet points)
- Avoid repetition
- Focus only on key ideas
- Do NOT explain unnecessarily

If answer is not found, say:
"I cannot find the answer in the document."

Format:
- 3–4 bullet points ONLY
- Each bullet = one key idea
- No paragraphs

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