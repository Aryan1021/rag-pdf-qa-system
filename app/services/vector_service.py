import os
from langchain_community.vectorstores import FAISS

VECTOR_DB_PATH = "vectorstore"


def create_vector_store(chunks, embedding_model):
    try:
        # Create vector store
        vector_store = FAISS.from_documents(chunks, embedding_model)

        # Ensure directory exists
        os.makedirs(VECTOR_DB_PATH, exist_ok=True)

        # Save locally
        vector_store.save_local(VECTOR_DB_PATH)

        return vector_store

    except Exception as e:
        raise Exception(f"Error creating vector store: {str(e)}")


def load_vector_store(embedding_model):
    try:
        if not os.path.exists(VECTOR_DB_PATH):
            raise Exception("Vector store not found. Upload a PDF first.")

        vector_store = FAISS.load_local(
            VECTOR_DB_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return vector_store

    except Exception as e:
        raise Exception(f"Error loading vector store: {str(e)}")