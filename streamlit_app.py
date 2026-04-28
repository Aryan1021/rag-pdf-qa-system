import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Chat", layout="wide")

st.title("🤖 RAG Chat Assistant")
st.caption("Chat with your documents")

# ----------------------------
# SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:
    st.header("📄 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Upload one or more PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        if st.button("Upload & Process"):
            with st.spinner("Processing PDFs..."):
                success = True

                for file in uploaded_files:
                    files = {
                        "file": (file.name, file, "application/pdf")
                    }
                    res = requests.post(f"{API_URL}/upload/", files=files)

                    if res.status_code != 200:
                        success = False
                        break

                if success:
                    st.success("All PDFs uploaded successfully!")
                    st.session_state.pdf_uploaded = True
                else:
                    st.error("Error uploading PDFs")

    st.divider()

    # 🧹 Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

    st.divider()
    st.info("⚠️ Upload PDFs before asking questions")

# ----------------------------
# DISPLAY CHAT
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# CHAT INPUT
# ----------------------------
if prompt := st.chat_input("Ask something..."):

    if not st.session_state.pdf_uploaded:
        st.warning("Please upload PDFs first.")
        st.stop()

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()

        with st.spinner("Thinking..."):
            response = requests.post(
                f"{API_URL}/query/",
                json={"question": prompt}
            )

        if response.status_code == 200:
            data = response.json()
            full_answer = data["answer"]

            # ----------------------------
            # STREAMING EFFECT
            # ----------------------------
            streamed_text = ""
            for char in full_answer:
                streamed_text += char
                placeholder.markdown(streamed_text)
                time.sleep(0.01)

            # Save assistant message
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_answer
            })

            # ----------------------------
            # CONTEXT VIEWER
            # ----------------------------
            with st.expander("📄 View Context Used"):
                for i, chunk in enumerate(data["context_used"], 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.write(chunk)

        else:
            st.error("Error generating response")