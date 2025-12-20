from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

def build_rag_chain(retriever):
    # 1️⃣ Définir le LLM local Ollama
    llm = Ollama(
        model="mistral",       # nom du modèle local Ollama
        temperature=0,
        base_url="http://127.0.0.1:11434"  # si Ollama tourne en local
    )

    # 2️⃣ Créer le prompt
    prompt = ChatPromptTemplate.from_template("""
Answer the question ONLY using the context below:

{context}

Question: {question}
""")

    # 3️⃣ Chaîner retriever + prompt + LLM
    return (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

def format_docs(docs):
    # On extrait la page_content de chaque document et on les joint
    return "\n\n".join(doc.page_content for doc in docs)