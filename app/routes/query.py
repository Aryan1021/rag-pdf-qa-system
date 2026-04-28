from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.embedding_service import get_embedding_model
from app.services.vector_service import load_vector_store

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/")
async def query_documents(request: QueryRequest):
    try:
        # Load embedding model
        embedding_model = get_embedding_model()

        # Load FAISS vector store
        vector_store = load_vector_store(embedding_model)

        # Perform similarity search
        results = vector_store.similarity_search(request.question, k=3)

        # Extract text content
        retrieved_chunks = [doc.page_content for doc in results]

        return {
            "question": request.question,
            "retrieved_chunks": retrieved_chunks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))