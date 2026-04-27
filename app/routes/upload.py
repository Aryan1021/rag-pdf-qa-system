import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf

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

        return {
            "filename": file.filename,
            "pages": extracted_data["pages"],
            "message": "PDF uploaded and processed successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))