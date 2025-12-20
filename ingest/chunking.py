from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(texts: list) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []
    for text in texts:
        chunks.extend(splitter.split_text(text))

    return chunks
