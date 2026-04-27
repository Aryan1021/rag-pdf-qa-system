from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        return embeddings
    except Exception as e:
        raise Exception(f"Error loading embedding model: {str(e)}")