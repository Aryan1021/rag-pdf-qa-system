import os
from langchain_community.vectorstores import FAISS
from app.utils.logger import get_logger

logger = get_logger(__name__)

VECTOR_DB_PATH = "vectorstore"

def create_vector_store(chunks, embedding_model):
    try:
        os.makedirs(VECTOR_DB_PATH, exist_ok=True)

        # ✅ Check if vector DB already exists
        if os.path.exists(os.path.join(VECTOR_DB_PATH, "index.faiss")):
            logger.info("Existing vector store found. Loading and appending data.")

            db = FAISS.load_local(
                VECTOR_DB_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )

            db.add_documents(chunks)  # ✅ Append new data

        else:
            logger.info("Creating new vector store.")
            db = FAISS.from_documents(chunks, embedding_model)

        # Save updated DB
        db.save_local(VECTOR_DB_PATH)

        logger.info("Vector store updated successfully")

    except Exception as e:
        logger.error(f"Vector store creation failed: {str(e)}")
        raise Exception("Failed to create/update vector store")


def load_vector_store(embedding_model):
    try:
        if not os.path.exists(os.path.join(VECTOR_DB_PATH, "index.faiss")):
            raise Exception("Vector store not found")

        db = FAISS.load_local(
            VECTOR_DB_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        logger.info("Vector store loaded successfully")

        return db

    except Exception as e:
        logger.error(f"Vector store loading failed: {str(e)}")
        raise Exception("Vector store not found. Upload PDF first.")