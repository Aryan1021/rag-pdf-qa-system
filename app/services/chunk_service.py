from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utils.logger import get_logger

logger = get_logger(__name__)

def chunk_text(documents):
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(documents)

        logger.info(f"Generated {len(chunks)} chunks")

        return chunks

    except Exception as e:
        logger.error(f"Chunking failed: {str(e)}")
        raise Exception("Text chunking failed")