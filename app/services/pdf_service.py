from langchain_community.document_loaders import PyPDFLoader
from app.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text_from_pdf(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        logger.info(f"PDF loaded successfully: {file_path}")

        return {
            "pages": len(documents),
            "documents": documents
        }

    except Exception as e:
        logger.error(f"PDF extraction failed: {str(e)}")
        raise Exception("Failed to extract text from PDF")