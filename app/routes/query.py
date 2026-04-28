from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.embedding_service import get_embedding_model
from app.services.vector_service import load_vector_store
from app.services.rag_service import generate_answer

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/")
async def query_documents(request: QueryRequest):
    try:
        # Load embedding model
        embedding_model = get_embedding_model()

        # Load vector store
        vector_store = load_vector_store(embedding_model)

        # Retrieve relevant chunks
        results = vector_store.similarity_search(request.question, k=3)
        retrieved_chunks = [doc.page_content for doc in results]

        # Generate answer using RAG
        answer = generate_answer(retrieved_chunks, request.question)

        return {
            "question": request.question,
            "answer": answer,
            "context_used": retrieved_chunks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))