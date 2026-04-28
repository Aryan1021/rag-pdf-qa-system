import os
from langchain_community.vectorstores import FAISS
from app.utils.logger import get_logger

logger = get_logger(__name__)

VECTOR_DB_PATH = "vectorstore"

def create_vector_store(chunks, embedding_model):
    try:
        db = FAISS.from_documents(chunks, embedding_model)
        os.makedirs(VECTOR_DB_PATH, exist_ok=True)
        db.save_local(VECTOR_DB_PATH)

        logger.info("Vector store created and saved")

    except Exception as e:
        logger.error(f"Vector store creation failed: {str(e)}")
        raise Exception("Failed to create vector store")


def load_vector_store(embedding_model):
    try:
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