import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import chunk_text
from app.services.embedding_service import get_embedding_model
from app.services.vector_service import create_vector_store

router = APIRouter()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Extract text
        extracted_data = extract_text_from_pdf(file_path)

        # Chunk text
        chunks = chunk_text(extracted_data["documents"])

        # Generate embeddings
        embedding_model = get_embedding_model()

        # Store in FAISS
        create_vector_store(chunks, embedding_model)

        return {
            "filename": file.filename,
            "pages": extracted_data["pages"],
            "chunks": len(chunks),
            "message": "PDF processed and stored in vector database"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))