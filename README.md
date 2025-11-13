# Build a Local RAG Pipeline with Db2 and OpenAI

This project walks through a full Retrieval-Augmented Generation (RAG) pipeline using **OpenAI for embedding + answer generation** and **IBM Db2** as the vector database with native `VECTOR` support.

The pipeline combines:

- **Embedding generation using OpenAI (text-embedding-3-small/large)**
- **Vector storage and similarity search inside IBM Db2**
- **LLM answer generation using OpenAI GPT models**

Most steps—cleaning source text, chunking, embedding, vector insert, retrieval, and prompt construction—are implemented in pure Python and structured to be easily modified.  
You can adapt the workflow to any other vector DB or LLM by replacing only a few components.

---

## What You’ll Learn

- How to clean and segment HTML/text using sentence-aware chunking  
- How to generate embeddings with OpenAI’s embedding models  
- How to store vector data inside Db2 using the `VECTOR(1536, FLOAT32)` column type  
- How to perform **vector similarity search** in Db2 using `VECTOR_DISTANCE`  
- How to build grounded prompts from retrieved chunks  
- How to call OpenAI GPT models to generate context-based final answers  

---

# RAG Pipeline Overview

```
Source Webpage/Text
        │
   Text Cleaning
        │
  Sentence-based Chunking
        │
    OpenAI Embeddings
        │
 Db2 VECTOR Storage (VECTOR(1536,FLOAT32))
        │
Top-K Vector Search (VECTOR_DISTANCE)
        │
  Context Assembly for LLM
        │
 OpenAI GPT Answer Generation
```

---

# Setup Instructions

To set up the environment on a Red Hat–based Linux system (e.g., RHEL 9.4):

```bash
bash setup.sh
```

The setup script performs:

- Installation of system packages (Python, compilers, SSL libraries)  
- Creation and activation of a Python virtual environment  
- Installation of Python dependencies via `requirements.txt`  
- Retrieval of helper utilities required for Db2 notebook integration  

---

# Running the Notebook

To launch the demonstration notebook:

```bash
source .venv/bin/activate
jupyter notebook rag-db2-demo.ipynb
```

Inside the notebook, you will:

- Load and clean an HTML web page using `trafilatura`  
- Chunk the content using spaCy sentence segmentation with overlap  
- Generate embeddings via OpenAI APIs  
- Insert embeddings into Db2 into a `VECTOR` column  
- Run vector similarity search using:

  ```sql
  VECTOR_DISTANCE(embedding, query_embedding, EUCLIDEAN)
  ```

- Build prompts from retrieved context  
- Get final grounded responses via OpenAI GPT models  

---

# Environment Configuration

A `.env` file is required in the project root. Example:

```text
# OpenAI credentials
OPENAI_API_KEY=your-openai-api-key

# Db2 connection
database=SAMPLE
hostname=localhost
port=50000
protocol=tcpip
uid=db2inst1
pwd=your-db2-password
```


---

# Project Layout

```
.
├── rag-db2-demo.ipynb        # Full RAG workflow notebook
├── rag_db2_openai.py         # Script version of the RAG pipeline
├── setup.sh                  # Environment setup script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (ignored)
└── README.md                 # Project documentation
```

---

# Notes

- Embeddings are generated using **OpenAI**, removing the need for local models  
- Vector storage & similarity search happen natively inside **Db2**  
- All components (cleaning, chunking, vector search, prompting) are modular  
- This design avoids external vector DBs like Pinecone/FAISS/Chroma  
- The entire flow is transparent and educational  

---

# Adaptability

This project is intentionally modular.  
You can easily adapt it to:

- PostgreSQL + pgvector  
- Chroma / FAISS  
- Milvus / Pinecone  
- Other embedding models (Cohere, HuggingFace, Gemini)  
- Other LLMs (Claude, Gemini, Llama-3, Watsonx.ai)

If you're looking to build a grounded, local-first RAG workflow with full control over embedding, chunking, vector search, and LLM output, this project provides a solid reference implementation.

