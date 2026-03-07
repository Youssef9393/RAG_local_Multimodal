🤖 RAG Multimodal Local (PDF & Vidéo)

Application RAG (Retrieval-Augmented Generation) locale permettant de poser des questions sur des documents PDF et des vidéos, en combinant FAISS, LangChain et un LLM local (Ollama / Mistral) via une interface Streamlit.

<img width="1903" height="933" alt="image" src="https://github.com/user-attachments/assets/f31ed8a6-464b-4f15-afb8-c08d8a7fc4e1" />
<img width="1263" height="663" alt="image" src="https://github.com/user-attachments/assets/956d351c-d4d2-4855-a556-542d84231689" />


Project Requirements

# 📚 Local RAG System — Document

A **100% local Retrieval-Augmented Generation (RAG) system** that ingests **documents **, converts them into embeddings, performs **semantic search**, and answers questions using a **local LLM**.

The system guarantees **full privacy** because **no external APIs are used**. All processing (embeddings, vector search, LLM inference) runs **locally on your machine**.

---

---

# ⚙️ Installation

```bash
git clone https://github.com/yourusername/local-rag-system.git
cd local-rag-system
python -m venv venv
# Start Chat Interface
streamlit run app/streamlit_app.py
pip install -r requirements.txt
# Architecture Overview

This project implements a complete **RAG pipeline** composed of two major phases:

## Augmentation (Retrieval Pipeline)

1. Document   
2. Text extraction or speech transcription  
3. Intelligent chunking  
4. Embedding generation  
5. Vector storage using **FAISS**  
6. Semantic similarity search  

## Generation

1. Retrieve relevant chunks  
2. Build a prompt with retrieved context  
3. Send prompt to **local LLM (Ollama)**  
4. Generate a contextual response  

---

# ✨ Features

## Document Ingestion

- Automatic **PDF ingestion**
- Multi-page support
- Efficient text extraction
- Large document handling

---

Features:

- Automatic speech-to-text
- Language detection
- Optional timestamp transcription

---

## Intelligent Chunking

- Context-aware splitting
- Configurable chunk size
- Configurable overlap
- Preserves semantic meaning

---

## Embedding Generation

Fully local embedding generation.

Supported models:

- **BGE**
- **E5**
- **SBERT**

Features:

- Batch processing
- High performance

---

## Vector Storage

Vector database powered by **FAISS**

Capabilities:

- Persistent storage
- Fast similarity search
- Large dataset handling

---

## Semantic Search

- Query embedding generation
- Cosine similarity search
- Top-K retrieval
- Ranked results

---

## Local LLM Response Generation

Uses **Ollama** to run LLMs locally.

Benefits:

- Fully offline
- Context-based answers
- Reduced hallucinations
- Configurable prompts

---

## Conversational Interface

Interactive chatbot built with **Streamlit**.

Features:

- Chat interface
- Chat history
- Real-time responses
- Document-based Q&A

---

## Privacy & Security

✔ 100% Local execution  
✔ No data sent to external servers  
✔ Local storage for all files and models  

---

# Project Structure

<img width="478" height="565" alt="image" src="https://github.com/user-attachments/assets/91707cb6-6f07-4830-9c46-5c49c2514847" />

