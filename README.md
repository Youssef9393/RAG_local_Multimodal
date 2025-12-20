🤖 RAG Multimodal Local (PDF & Vidéo)

Application RAG (Retrieval-Augmented Generation) locale permettant de poser des questions sur des documents PDF et des vidéos, en combinant FAISS, LangChain et un LLM local (Ollama / Mistral) via une interface Streamlit.

<img width="1903" height="933" alt="image" src="https://github.com/user-attachments/assets/f31ed8a6-464b-4f15-afb8-c08d8a7fc4e1" />
<img width="1055" height="543" alt="image" src="https://github.com/user-attachments/assets/7a80518f-b8d1-4cba-b652-88d020adc323" />


📌 Fonctionnalités

📄 Ingestion automatique des PDF

🎥 Transcription des vidéos → texte

✂️ Chunking intelligent des documents

🧠 Génération d’embeddings

📦 Stockage vectoriel avec FAISS

🔍 Recherche sémantique (Top-K)

🤖 Génération de réponses via LLM local

💬 Interface conversationnelle avec Streamlit

🔒 100% local & données privées

🏗️ Architecture du projet
RAG_Local_Multimodal/
│
├── data/
│   ├── documents/          # PDFs
│   └── videos/             # Vidéos
│
├── ingest/
│   ├── pdf_loader.py       # Extraction texte PDF
│   ├── video_loader.py     # Vidéo → Audio → Texte
│   ├── chunking.py         # Découpage des documents
│
├── vector_store/
│   └── faiss_store.py      # Construction FAISS
│
├── rag/
│   ├── retriever.py        # Logique de récupération
│   └── generator.py        # Chaîne RAG (Prompt + LLM)
│
├── app.py                  # Application Streamlit
├── config.py               # Configuration globale
├── requirements.txt
└── README.md
