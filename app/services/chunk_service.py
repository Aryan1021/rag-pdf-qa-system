from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(documents):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,       # size of each chunk
            chunk_overlap=100     # overlap for context continuity
        )

        chunks = text_splitter.split_documents(documents)

        return chunks

    except Exception as e:
        raise Exception(f"Error during text chunking: {str(e)}")