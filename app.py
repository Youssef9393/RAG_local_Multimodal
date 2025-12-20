import streamlit as st
import os

from ingest.pdf_loader import load_pdfs_from_folder
from ingest.video_loader import load_videos_from_folder
from ingest.chunking import chunk_documents
from vector_store.faiss_store import build_faiss
from rag.generator import build_rag_chain

# -----------------------------
# Config & Paths
# -----------------------------
DATA_PDF = r"C:\Users\GK\OneDrive\Bureau\RAG_Local_Mutimodal\data\documents"
DATA_VIDEO = r"C:\Users\GK\OneDrive\Bureau\RAG_Local_Mutimodal\data\videos"

st.set_page_config(
    page_title="RAG Chat",
    layout="wide"
)

st.title("🤖 RAG Multimodal Chat")

# -----------------------------
# Load RAG (cached)
# -----------------------------
@st.cache_resource(show_spinner="🔄 Loading knowledge base...")
def load_rag():
    if not os.path.exists(DATA_PDF) or not os.path.exists(DATA_VIDEO):
        st.error(" Data folders not found.")
        st.stop()

    pdf_texts = load_pdfs_from_folder(DATA_PDF)
    video_texts = load_videos_from_folder(DATA_VIDEO)

    all_texts = pdf_texts + video_texts

    if not all_texts:
        st.warning("⚠️ Aucun document trouvé.")
        return None

    chunks = chunk_documents(all_texts)
    vectorstore = build_faiss(chunks)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    rag_chain = build_rag_chain(retriever)

    return rag_chain

rag_chain = load_rag()

# -----------------------------
# Initialiser l'historique
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # [{role: "user"/"assistant", content: "..."}]

# -----------------------------
# Sidebar : Historique
# -----------------------------
with st.sidebar:
    st.title("📚 Historique")

    if not st.session_state.messages:
        st.caption("Aucune conversation")
    else:
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f"**🧑 {i//2 + 1}.** {msg['content']}")

    if st.button("🗑️ Effacer l'historique"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Affichage du chat
# -----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Input ChatGPT-like
# -----------------------------
user_input = st.chat_input("Posez votre question...")

if user_input and rag_chain:
    # 🔹 Ajouter message utilisateur
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Afficher immédiatement le message utilisateur
    with st.chat_message("user"):
        st.markdown(user_input)

    # Génération réponse
    with st.chat_message("assistant"):
        with st.spinner("🤖 Génération de la réponse..."):
            try:
                response = rag_chain.invoke(user_input)
                st.markdown(response)

                # 🔹 Sauvegarder réponse assistant
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )

            except Exception as e:
                error_msg = f"❌ Erreur : {e}"
                st.error(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg}
                )
