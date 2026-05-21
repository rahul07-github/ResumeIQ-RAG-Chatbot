<div align="center">

# 🧠 ResumeIQ — AI Resume Chatbot

### *Upload any resume. Ask anything. Get instant AI-powered answers.*

[![HuggingFace](https://img.shields.io/badge/🤗%20HuggingFace-Live%20Demo-ff9900?style=for-the-badge)](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/GPT--4o--mini-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=for-the-badge)](https://gradio.app)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-0467DF?style=for-the-badge)](https://faiss.ai)
[![License](https://img.shields.io/badge/License-View%20Only-red?style=for-the-badge)](#license)

<br/>

> **ResumeIQ** is an end-to-end Generative AI project built on a **RAG (Retrieval Augmented Generation)** pipeline.
> Upload any PDF or DOCX resume — and ask anything about it in natural language.

<br/>

![ResumeIQ Banner](https://img.shields.io/badge/Status-Live%20on%20HuggingFace-00d4aa?style=flat-square)
![Questions](https://img.shields.io/badge/Supports-PDF%20%7C%20DOCX-6c63ff?style=flat-square)
![Memory](https://img.shields.io/badge/Feature-Conversational%20Memory-ff6b6b?style=flat-square)

</div>

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Screenshots](#-screenshots)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [RAG Pipeline](#-rag-pipeline)
- [Problems Faced &amp; Solutions](#-problems-faced--solutions)
- [How to Run Locally](#-how-to-run-locally)
- [License](#-license)

---

## 🎯 Project Overview

**ResumeIQ** is a production-grade **Generative AI chatbot** that reads and understands any resume using the **RAG (Retrieval Augmented Generation)** technique.

Instead of asking an LLM to answer from its training data, ResumeIQ:

1. **Reads** the uploaded resume (PDF/DOCX)
2. **Chunks** it into small pieces
3. **Embeds** each chunk into vectors using OpenAI Embeddings
4. **Stores** them in a FAISS vector database
5. **Retrieves** the most relevant chunks for each question
6. **Generates** accurate, context-aware answers using GPT-4o-mini

> This ensures answers are **grounded in the actual resume** — not hallucinated by the model.

---

## 🚀 Live Demo

<div align="center">

### 👉 [Try ResumeIQ on HuggingFace Spaces](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)

> ⚠️ **Note:** You need an OpenAI API key to use this app.
> Get a free key at [platform.openai.com](https://platform.openai.com/api-keys)

</div>

---

## 📸 Screenshots

### Main Interface

```
┌─────────────────────────────────────────────────────────────┐
│  🧠 ResumeIQ — AI Resume Chatbot                            │
│  AI-powered resume analysis — Upload any resume instantly   │
├──────────────────────┬──────────────────────────────────────┤
│  🔑 OpenAI API Key   │  💡 Quick Questions                  │
│  ┌──────────────┐    │  [Who is this person?] [Skills?]     │
│  │ sk-...       │    │  [Internship?] [Projects?]           │
│  └──────────────┘    │                                      │
│                      │  ┌──────────────────────────────┐   │
│  📄 Upload Resume    │  │   Chat Window                │   │
│  ┌──────────────┐    │  │                              │   │
│  │ PDF or DOCX  │    │  │  You: Who is this person?    │   │
│  └──────────────┘    │  │  AI:  Rahul Kumar Jha is a  │   │
│  [Analyze Resume]    │  │  Data Scientist with...      │   │
│                      │  └──────────────────────────────┘   │
│  📋 File Info        │                                      │
│  File: resume.pdf    │  [Ask anything about resume...]      │
│  Chunks: 11          │                          [Send →]    │
│  Pages: 1            │                                      │
│  Status: Ready ✅    │                                      │
│                      │                                      │
│  [Save Chat as PDF]  │                                      │
│  [Clear All]         │                                      │
└──────────────────────┴──────────────────────────────────────┘
```

---

## ✨ Features

| Feature                           | Description                                          |
| --------------------------------- | ---------------------------------------------------- |
| 📄**Multi-Format Upload**   | Supports both PDF and DOCX resume formats            |
| 🧠**RAG Pipeline**          | Retrieves relevant context before generating answers |
| 💬**Conversational Memory** | Remembers previous questions in the same session     |
| ⚡**Quick Question Chips**  | 8 pre-built questions for instant analysis           |
| 📊**File Info Dashboard**   | Shows chunks, pages, and status in real-time         |
| 💾**Save Chat as PDF**      | Export entire Q&A session as a formatted PDF         |
| 🗑️**Clear & Reset**       | One-click reset for new resume analysis              |
| 🔒**Privacy First**         | API key never stored — all processing is stateless  |
| 🌐**Cloud Deployed**        | Live on HuggingFace Spaces — no installation needed |

---

## 🛠️ Tech Stack

### Core AI/ML

| Technology                   | Version                | Purpose                      |
| ---------------------------- | ---------------------- | ---------------------------- |
| **LangChain**          | 0.x                    | RAG pipeline orchestration   |
| **LangChain Classic**  | latest                 | ConversationalRetrievalChain |
| **OpenAI GPT-4o-mini** | latest                 | Answer generation (LLM)      |
| **OpenAI Embeddings**  | text-embedding-ada-002 | Text vectorization           |
| **FAISS**              | 1.7.x                  | Vector similarity search     |

### Document Processing

| Technology                               | Purpose              |
| ---------------------------------------- | -------------------- |
| **PyMuPDF**                        | PDF text extraction  |
| **Docx2txt**                       | DOCX text extraction |
| **RecursiveCharacterTextSplitter** | Smart text chunking  |

### UI & Deployment

| Technology                   | Purpose            |
| ---------------------------- | ------------------ |
| **Gradio 5.31.0**      | Interactive web UI |
| **HuggingFace Spaces** | Cloud deployment   |
| **fpdf2**              | Chat PDF export    |

---

## 📁 Project Structure

```
ResumeIQ-RAG-Chatbot/
│
├── 📓 Notebook/
│   └── Rag_langchain.ipynb       ← Development & testing notebook
│
├── 📁 Project/
│   ├── app.py                    ← Main Gradio application
│   ├── resume_chatbot.py         ← Streamlit version (local)
│   └── faiss_index/              ← Saved FAISS vector store
│
├── 📁 Data/
│   ├── Rahul01.pdf               ← Sample resume 1
│   └── Sonu_Jha_Resume.pdf       ← Sample resume 2
│
├── 📁 saved_resumes/             ← Saved resume files
├── 📁 saved_chats/               ← Exported chat PDFs
│
├── requirements.txt              ← Python dependencies
├── .gitignore                    ← Git ignore rules
└── README.md                     ← This file
```

---

## 🔄 RAG Pipeline

```
┌─────────────┐
│  PDF/DOCX   │
│   Upload    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PyMuPDF /  │   Extract raw text
│  Docx2txt   │   from document
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Text     │   Remove special chars,
│  Cleaning   │   normalize whitespace
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Text      │   chunk_size=500
│  Splitting  │   chunk_overlap=100
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  OpenAI     │   text-embedding-ada-002
│ Embeddings  │   → number vectors
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    FAISS    │   Store all vectors
│ Vector Store│   for similarity search
└──────┬──────┘
       │
  User Question
       │
       ▼
┌─────────────┐
│  Retriever  │   Find top-k most
│   k = all   │   similar chunks
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  GPT-4o-mini│   Read chunks +
│    (LLM)    │   Generate answer
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Final    │
│    Answer   │
└─────────────┘
```

---

## 🐛 Problems Faced & Solutions

### Problem 1 — Wrong Import Paths

```python
# ❌ Error: No module named 'langchain.chains'
from langchain.chains import ConversationalRetrievalChain

# ✅ Solution: Use langchain_classic
from langchain_classic.chains import ConversationalRetrievalChain
```

**Root Cause:** LangChain v1.x removed legacy chains from main package.

---

### Problem 2 — Tuple Object Error

```
AttributeError: 'tuple' object has no attribute 'page_content'
```

**Root Cause:** PDF loader returned tuples instead of Document objects.

```python
# ✅ Solution: Convert tuples to Documents
from langchain_core.documents import Document
docs = [Document(page_content=d[0], metadata=d[1])
        if isinstance(d, tuple) else d for d in docs]
```

---

### Problem 3 — Wrong Answers ("Not found in document")

**Root Cause:** Retriever was fetching wrong chunks — name chunk was not being retrieved.

```python
# ❌ k=3 — missed important chunks
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ✅ Solution: Retrieve ALL chunks for small documents
retriever = vectorstore.as_retriever(search_kwargs={"k": len(chunks)})
```

---

### Problem 4 — GPU Memory Crash

```
cudaMalloc failed: out of memory (status code: 500)
GGML_ASSERT(ctx->mem_buffer != NULL) failed
```

**Root Cause:** Local LLM (llama3.2) exceeded GPU VRAM on RTX 2050 (4GB).
**Solution:** Switched to OpenAI API (GPT-4o-mini) — cloud-based, no local GPU needed.

---

### Problem 5 — Gradio Version Incompatibility (HuggingFace)

```
TypeError: Chatbot.__init__() got unexpected argument 'bubble_full_width'
TypeError: Chatbot.__init__() got unexpected argument 'type'
UserWarning: theme, css moved to launch()
```

**Root Cause:** HuggingFace installs latest Gradio — breaking changes in v5/v6.

```txt
# ✅ Solution: Pin exact version in requirements.txt
gradio==5.31.0
```

---

### Problem 6 — conda Not Recognized in PowerShell

```
'conda' is not recognized as an internal or external command
```

**Solution:** Used `sys.executable` to run pip/streamlit from correct environment:

```python
import sys, subprocess
subprocess.run([sys.executable, "-m", "pip", "install", "package"])
```

---

## 💻 How to Run Locally

### Prerequisites

- Python 3.11+
- Anaconda (recommended)
- OpenAI API Key
- Ollama (optional — for local LLM)

### Installation

```bash
# Clone the repository
git clone https://github.com/rahul07-github/ResumeIQ-RAG-Chatbot.git
cd ResumeIQ-RAG-Chatbot

# Create conda environment
conda create -n resumeiq python=3.11
conda activate resumeiq

# Install dependencies
pip install -r requirements.txt
```

### Run Gradio App

```bash
python app.py
# Open: http://localhost:7860
```

### Run Streamlit App

```bash
streamlit run resume_chatbot.py
# Open: http://localhost:8501
```

### Environment Variables

```bash
# Create .env file
OPENAI_API_KEY=sk-your-key-here
```

---

## 📦 Requirements

```txt
gradio==5.31.0
langchain
langchain-community
langchain-openai
langchain-classic
langchain-core
langchain-text-splitters
faiss-cpu
pymupdf
docx2txt
fpdf2
openai
tiktoken
```

---

## 👨‍💻 Author

<div align="center">

**Rahul Kumar Jha**

*Data Analyst | ML Engineer | Fresher 2026*

[![Portfolio](https://img.shields.io/badge/Portfolio-rahul07--github.github.io-6c63ff?style=for-the-badge)](https://rahul07-github.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rahulkumarjha)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/rahul07-github)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Profile-ff9900?style=for-the-badge)](https://huggingface.co/rahulkumarjha)

📧 rahulkumarjha9643@gmail.com | 📍 Bhopal, India

</div>

---

## 📄 License

```
Copyright (c) 2026 Rahul Kumar Jha

VIEW-ONLY LICENSE

This project and its source code are made available for
viewing and educational reference only.

You MAY:
  ✅ Read and study the source code
  ✅ Download for personal reference
  ✅ Share the repository link

You MAY NOT:
  ❌ Copy or reproduce the code
  ❌ Use in your own projects
  ❌ Distribute or sell
  ❌ Modify and republish
  ❌ Claim as your own work

For permissions beyond viewing,
contact: rahulkumarjha9643@gmail.com
```

---

<div align="center">

**⭐ If you found this project helpful, please star the repository!**

*Built with ❤️ by Rahul Kumar Jha | Powered by LangChain + OpenAI + FAISS*

[![HuggingFace Demo](https://img.shields.io/badge/🤗%20Live%20Demo-Try%20Now-ff9900?style=for-the-badge)](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)

</div>
