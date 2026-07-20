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


## Project Requirements

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

```bash
git clone https://github.com/yourusername/local-rag-system.git
cd local-rag-system
python -m venv venv
# Start Chat Interface
streamlit run app/streamlit_app.py
pip install -r requirements.txt```

# Architecture Overview`



---

---

# ⚙️ Installation


# Local Multimodal RAG System (PDF & Video)

A fully local **Retrieval-Augmented Generation (RAG)** application for querying **PDF documents and videos** using **FAISS**, **LangChain**, and a **local LLM (Ollama / Mistral)** through a **Streamlit web interface**.

<figure>
  <img src="https://github.com/user-attachments/assets/f31ed8a6-464b-4f15-afb8-c08d8a7fc4e1" alt="Streamlit interface" width="100%" />
  <figcaption>Streamlit interface</figcaption>
</figure>

<figure>
  <img src="https://github.com/user-attachments/assets/956d351c-d4d2-4855-a556-542d84231689" alt="Document retrieval and answer generation" width="75%" />
  <figcaption>Document retrieval and answer generation</figcaption>
</figure>

---

## Overview

This project implements a **100% local multimodal RAG pipeline** capable of:

* ingesting **PDF documents** and **video/audio files**,
* extracting text and speech transcripts,
* generating **vector embeddings**,
* storing embeddings in a **FAISS vector database**,
* performing **semantic search**, and
* generating contextual answers with a **local large language model**.

All components run **locally on your machine**. No external APIs are required, ensuring **data privacy and offline operation**.

---

## Features

### Document ingestion

* Automatic PDF ingestion
* Multi-page document support
* Efficient text extraction
* Large document handling

### Video and audio transcription

* Automatic speech-to-text transcription
* Language detection
* Optional timestamp generation
* Support for common video formats

### Intelligent chunking

* Context-aware text splitting
* Configurable chunk size
* Configurable overlap
* Preservation of semantic continuity

### Embedding generation

Supported local embedding models:

* **BGE**
* **E5**
* **Sentence-BERT (SBERT)**

Capabilities:

* Batch embedding generation
* GPU acceleration (if available)
* Fully offline processing

### Vector storage

Powered by **FAISS**:

* Persistent vector storage
* Fast similarity search
* Scalable retrieval for large collections

### Semantic retrieval

* Query embedding generation
* Cosine similarity search
* Top-K retrieval
* Ranked relevant passages

### Local LLM generation

Integrated with **Ollama**:

* Offline inference
* Context-grounded answers
* Reduced hallucinations
* Customizable prompts and parameters

### Conversational interface

Built with **Streamlit**:

* Interactive chat interface
* Conversation history
* Real-time response streaming
* Document-based question answering

### Privacy and security

* 100% local execution
* No external API calls
* Local storage of documents, embeddings, and models

---

## Architecture

The system is composed of two main phases.

### Retrieval pipeline

1. Document or video ingestion
2. Text extraction or speech transcription
3. Intelligent chunking
4. Embedding generation
5. FAISS vector indexing
6. Semantic similarity search

### Generation pipeline

1. Retrieve relevant chunks
2. Build a prompt with retrieved context
3. Send the prompt to a local LLM via **Ollama**
4. Generate a contextual answer

<figure>
  <img src="https://github.com/user-attachments/assets/91707cb6-6f07-4830-9c46-5c49c2514847" alt="Project architecture" width="70%" />
  <figcaption>Project architecture</figcaption>
</figure>

---



---

## Installation

### Prerequisites

* Python **3.10+**
* **Ollama** installed locally
* Git

Install Ollama from the official website:

* https://ollama.com

Pull a local model (example with Mistral):

```bash
ollama pull mistral
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

## Technology stack

<Table columnSizing="equal" rowDivider={{"size":1,"color":"default"}}><Table.Row header><Table.Cell>Component</Table.Cell><Table.Cell align="center">Technology</Table.Cell></Table.Row><Table.Row><Table.Cell>Frontend</Table.Cell><Table.Cell align="center">Streamlit</Table.Cell></Table.Row><Table.Row><Table.Cell>RAG Framework</Table.Cell><Table.Cell align="center">LangChain</Table.Cell></Table.Row><Table.Row><Table.Cell>Vector Database</Table.Cell><Table.Cell align="center">FAISS</Table.Cell></Table.Row><Table.Row><Table.Cell>LLM Runtime</Table.Cell><Table.Cell align="center">Ollama</Table.Cell></Table.Row><Table.Row><Table.Cell>LLM</Table.Cell><Table.Cell align="center">Mistral / Llama / Qwen</Table.Cell></Table.Row><Table.Row><Table.Cell>Embeddings</Table.Cell><Table.Cell align="center">BGE / E5 / SBERT</Table.Cell></Table.Row><Table.Row><Table.Cell>PDF Processing</Table.Cell><Table.Cell align="center">PyMuPDF / pdfplumber</Table.Cell></Table.Row><Table.Row><Table.Cell>Speech Recognition</Table.Cell><Table.Cell align="center">Whisper</Table.Cell></Table.Row><Table.Row><Table.Cell>Backend</Table.Cell><Table.Cell align="center">Python</Table.Cell></Table.Row></Table>

---

## Example workflow

```text
User Question
      |
      v
Query Embedding
      |
      v
FAISS Similarity Search
      |
      v
Retrieve Top-K Chunks
      |
      v
Build Prompt with Context
      |
      v
Ollama (Mistral)
      |
      v
Generated Answer
```

---

## Advantages

* **Fully offline** operation
* **No external API costs**
* **Privacy-preserving**
* **Supports both documents and videos**
* **Modular and extensible architecture**
* **Suitable for research, education, and enterprise environments**

---

## Future improvements

* Hybrid search (BM25 + dense retrieval)
* Reranking with cross-encoders
* Multi-user document collections
* Streaming token generation
* Evaluation framework for retrieval quality
* Docker and Kubernetes deployment

---

## Contributing

Contributions are welcome.

```bash
# Create a feature branch
git checkout -b feature/my-feature

# Commit your changes
git commit -m "Add my feature"

# Push to GitHub
git push origin feature/my-feature
```

Then open a Pull Request.

---

## License

This project is released under the **MIT License**.

---

## Acknowledgments

This project uses the following open-source technologies:

* **LangChain**
* **FAISS**
* **Ollama**
* **Streamlit**
* **Whisper**
* **Sentence Transformers**
* **PyMuPDF**

---

## Contact

**Youssef ELJAOUHARY**
Master’s Student in Web Intelligence and Data Science
Sidi Mohamed Ben Abdellah University, Fez, Morocco

GitHub: https://github.com/Youssef9393
