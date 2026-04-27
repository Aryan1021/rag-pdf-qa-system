from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        # Combine all page contents
        full_text = "\n".join([doc.page_content for doc in documents])

        return {
            "pages": len(documents),
            "text": full_text,
            "documents": documents  # useful for later steps
        }

    except Exception as e:
        raise Exception(f"Error extracting text: {str(e)}")