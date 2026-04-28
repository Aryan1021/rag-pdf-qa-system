from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.logger import get_logger

from app.services.embedding_service import get_embedding_model
from app.services.vector_service import load_vector_store
from app.services.rag_service import generate_answer

logger = get_logger(__name__)

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/")
async def query_documents(request: QueryRequest):
    try:
        embedding_model = get_embedding_model()
        vector_store = load_vector_store(embedding_model)

        results = vector_store.similarity_search(request.question, k=2)
        chunks = [doc.page_content for doc in results]

        answer = generate_answer(chunks, request.question)

        return {
            "question": request.question,
            "answer": answer,
            "context_used": chunks
        }

    except Exception as e:
        logger.error(f"Query failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Please try again."
        )