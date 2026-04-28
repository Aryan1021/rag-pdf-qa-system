# 🚀 RAG PDF Q&A System

An AI-powered full-stack application that allows users to upload PDF documents and interact with them using a ChatGPT-like interface powered by Retrieval-Augmented Generation (RAG).

---

## 📌 Overview

This project implements a complete **RAG pipeline**:

1. Upload one or more PDF documents
2. Extract and process text
3. Split text into chunks
4. Convert text into embeddings
5. Store embeddings in FAISS vector database
6. Retrieve relevant context for user queries
7. Generate answers using a local LLM (Ollama)

---

## 🧠 Features

* 📄 **Multi-PDF Upload & Processing**
* ✂️ **Smart Text Chunking**
* 🔎 **Semantic Search using FAISS**
* 🧠 **Context-Aware Answer Generation**
* 🤖 **Local LLM (Ollama - Mistral)**
* 💬 **ChatGPT-like UI (Streamlit)**
* ⚡ **Streaming Responses (Typing Effect)**
* 🧵 **Conversation Memory (Session-based)**
* 📊 **Structured Output (Summary + Bullet Points)**
* 📝 **Logging & Error Handling**

---

## 🛠️ Tech Stack

| Layer           | Technology            |
| --------------- | --------------------- |
| Backend         | FastAPI               |
| Frontend        | Streamlit             |
| LLM             | Ollama (Mistral)      |
| Embeddings      | Sentence Transformers |
| Vector DB       | FAISS                 |
| Framework       | LangChain             |
| File Processing | PyPDFLoader           |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/rag-pdf-qa-system.git
cd rag-pdf-qa-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama (Local LLM)

Download from:
👉 https://ollama.com

Then run:

```bash
ollama pull mistral
```

---

### 5️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

---

### 6️⃣ Run Frontend

```bash
streamlit run streamlit_app.py
```

---

### 7️⃣ Start Ollama Model

```bash
ollama run mistral
```

---

## 🧪 API Endpoints

### 🔹 Upload PDF

```
POST /upload/
```

---

### 🔹 Query Documents

```
POST /query/
```

Example:

```json
{
  "question": "What is the purpose of the project?"
}
```

---

## 💬 UI Features

* ChatGPT-style conversational interface
* Streaming responses (typing effect)
* Multi-PDF querying
* Clear chat functionality
* Context viewer for retrieved chunks

---

## 📸 Sample Output

```json
{
  "answer": "Summary: Flutter-based system for digital inspection and PDF reporting.\n- Uses PDF generation packages\n- Includes scoring and grading logic\n- Generates structured reports\n- Improves inspection workflow efficiency"
}
```

---

## 📂 Project Structure

```
rag-pdf-qa-system/
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── config/
│   └── main.py
├── data/
├── vectorstore/
├── logs/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes

* Upload at least one PDF before querying
* Ollama must be running locally
* Logs are stored in `/logs/app.log`
* Multiple PDFs are supported (data is appended to vector store)

---

## 🚀 Future Improvements

* Document-level filtering (metadata-based retrieval)
* User authentication
* Cloud deployment (Docker + AWS)
* Real-time streaming from backend
* Chat history persistence (database)

---

## 👨‍💻 Author

**Aryan Raj**

---

## ⭐ If you found this useful

Give this repo a ⭐ and share it!
