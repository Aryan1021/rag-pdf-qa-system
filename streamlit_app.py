import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG PDF Q&A", layout="wide")

st.title("📄 RAG PDF Q&A System")
st.write("Upload a PDF and ask questions based on its content.")

# ------------------------
# PDF Upload Section
# ------------------------
st.header("📤 Upload PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    if st.button("Upload"):
        with st.spinner("Uploading and processing PDF..."):
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            response = requests.post(f"{API_URL}/upload/", files=files)

            if response.status_code == 200:
                st.success("PDF uploaded and processed successfully!")
                st.json(response.json())
            else:
                st.error("Upload failed")
                st.text(response.text)

# ------------------------
# Question Section
# ------------------------
st.header("❓ Ask a Question")

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{API_URL}/query/",
                json={"question": question}
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("🧠 Answer")
                st.write(data["answer"])

                with st.expander("📄 Context Used"):
                    for i, chunk in enumerate(data["context_used"], 1):
                        st.markdown(f"**Chunk {i}:**")
                        st.write(chunk)

            else:
                st.error("Error fetching answer")
                st.text(response.text)