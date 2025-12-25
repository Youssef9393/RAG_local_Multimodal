🤖 RAG Multimodal Local (PDF & Vidéo)

Application RAG (Retrieval-Augmented Generation) locale permettant de poser des questions sur des documents PDF et des vidéos, en combinant FAISS, LangChain et un LLM local (Ollama / Mistral) via une interface Streamlit.

<img width="1903" height="933" alt="image" src="https://github.com/user-attachments/assets/f31ed8a6-464b-4f15-afb8-c08d8a7fc4e1" />
<img width="1055" height="543" alt="image" src="https://github.com/user-attachments/assets/7a80518f-b8d1-4cba-b652-88d020adc323" />


Project Requirements

This project is a 100% local, privacy-preserving RAG system that ingests documents and videos, converts them into embeddings, and enables semantic search with conversational AI.

🧩 Functional Requirements
📄 Document Ingestion

Automatic ingestion of PDF files

Text extraction using reliable PDF parsers

Support for multi-page and large documents

🎥 Video Transcription

Accepts video files (.mp4, .mkv, .avi)

Automatic speech-to-text transcription

Language detection and normalization

Timestamped transcription support (optional)

✂️ Intelligent Chunking

Context-aware text chunking

Configurable chunk size and overlap

Preserves semantic coherence

Supports documents and transcriptions

🧠 Embedding Generation

Local embedding generation (no external APIs)

Support for open-source embedding models (e.g. BGE, E5, SBERT)

Batch processing for performance optimization

📦 Vector Storage

Vector indexing using FAISS

Persistent local storage

Fast similarity search on large datasets

🔍 Semantic Search

Top-K semantic retrieval

Cosine similarity metric

Query embedding generation

Ranked results with metadata

🤖 Local LLM Response Generation

Fully local LLM inference (CPU or GPU)

Uses retrieved chunks as context (RAG)

Configurable prompt templates

Hallucination reduction via grounded context

💬 Conversational Interface

Interactive chatbot interface using Streamlit

Chat history management

Real-time response streaming (optional)

User-friendly document querying

🔒 Privacy & Security

100% local execution

No data sent to external servers

All documents, embeddings, and models stored locally

⚙️ Non-Functional Requirements
Performance

Efficient chunking and embedding pipelines

Low-latency semantic search

Scalable to thousands of documents

Compatibility

Cross-platform (Linux, macOS, Windows)

Python 3.9+

Maintainability

Modular architecture

Clear separation of ingestion, retrieval, and generation

Well-documented codebase

<img width="478" height="565" alt="image" src="https://github.com/user-attachments/assets/50d8948a-880c-4157-81e8-4ae129f832a6" />
