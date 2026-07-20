## 🤖 RAG Multimodal Local (PDF & Vidéo)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![RAG](https://img.shields.io/badge/RAG-Multimodal-red)
![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-orange)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![Offline](https://img.shields.io/badge/Offline-100%25-success)

A **100% local Retrieval-Augmented Generation (RAG) system** that ingests **documents **, converts them into embeddings, performs **semantic search**, and answers questions using a **local LLM**.

The system guarantees **full privacy** because **no external APIs are used**. All processing (embeddings, vector search, LLM inference) runs **locally on your machine**.

<img width="1903" height="933" alt="image" src="https://github.com/user-attachments/assets/f31ed8a6-464b-4f15-afb8-c08d8a7fc4e1" />
<img width="1263" height="663" alt="image" src="https://github.com/user-attachments/assets/956d351c-d4d2-4855-a556-542d84231689" />

## Project structure

```text
local-rag-system/
├── app/
│   └── streamlit_app.py        # Streamlit interface
├── backend/
│   ├── ingestion/              # PDF and video ingestion
│   ├── processing/             # Chunking and preprocessing
│   ├── embeddings/             # Embedding generation
│   ├── vectorstore/            # FAISS index management
│   ├── llm/                    # Ollama integration
│   └── retrieval/              # Semantic search pipeline
├── data/
│   ├── documents/              # Input PDFs
│   ├── videos/                 # Input videos
│   └── transcripts/            # Generated transcripts
├── models/                     # Local embedding models
├── vectorstore/                # Persistent FAISS indexes
├── requirements.txt
└── README.md
```

### Clone the repository

```bash
git clone https://github.com/yourusername/local-rag-system.git
cd local-rag-system
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\\Scripts\\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the application

Start the Streamlit interface:

```bash
streamlit run app/streamlit_app.py
```

Open your browser at:

```text
http://localhost:8501
```

---

## Usage

### Index a PDF document

Place your PDF files in:

```text
data/documents/
```

The application will automatically process and index them.

### Index a video

Place video files in:

```text
data/videos/
```

The system will extract audio, generate a transcript, and create embeddings.

### Ask questions

Examples:

* *What is the main objective of the document?*
* *Summarize the methodology section.*
* *What was discussed in the video about neural networks?*
* *List the key findings and conclusions.*

---

## License

This project is released under the **MIT License**.

---

## Contact

**Youssef ELJAOUHARY**
Master’s Student in Web Intelligence and Data Science
Sidi Mohamed Ben Abdellah University, Fez, Morocco

GitHub: https://github.com/Youssef9393
