<div align="center">

# 🧠 ResumeIQ — AI Resume Chatbot

### *Upload any resume. Ask anything. Get instant answers.*

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/GPT--4o--mini-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://faiss.ai)
[![Gradio](https://img.shields.io/badge/Gradio-5.31-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Deployed-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)
[![License](https://img.shields.io/badge/License-Restricted_View_Only-red?style=for-the-badge)](LICENSE)

<br>

> **ResumeIQ** is an end-to-end AI-powered Resume Chatbot built using the RAG (Retrieval-Augmented Generation) pipeline.
> Upload any PDF or DOCX resume, ask natural language questions, and get accurate, context-aware answers instantly.

<br>

**[🚀 Live Demo — HuggingFace](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)** &nbsp;|&nbsp; **[💻 Local Run Guide](#-local-setup)** &nbsp;|&nbsp; **[📊 Pipeline](#-rag-pipeline)**

</div>

---

## 📸 Screenshots

<div align="center">

### 🖥️ Streamlit UI — Dark Theme
> Resume uploaded, analyzed, and ready to answer questions

```
[Add your Streamlit screenshot here]
Path: screenshots/streamlit_ui.png
```

### 🤗 HuggingFace Gradio — Live Deployment
> Live demo running on HuggingFace Spaces

```
[Add your HuggingFace screenshot here]
Path: screenshots/huggingface_ui.png
```

</div>

---

## 🎯 Project Overview

ResumeIQ solves a real-world problem — **manually reading resumes is slow and tedious.**

With ResumeIQ, you can:

- Upload **any resume** in PDF or DOCX format
- Ask questions like *"What are the technical skills?"* or *"Tell me about internship"*
- Get **accurate, context-based answers** powered by GPT-4o-mini
- **Save the full Q&A session** as a PDF report
- Use **Quick Question chips** for one-click common queries

This project demonstrates a complete **GenAI + RAG pipeline** — from document ingestion to conversational AI.

---

## ⚙️ Tools & Technologies

| Category | Tool | Purpose |
|---|---|---|
| **Language** | Python 3.11 | Core language |
| **LLM** | GPT-4o-mini (OpenAI) | Answer generation |
| **Embeddings** | OpenAI Embeddings | Text vectorization |
| **Vector Store** | FAISS | Similarity search |
| **RAG Framework** | LangChain Classic | Chain orchestration |
| **PDF Loader** | PyMuPDF | Document parsing |
| **Text Splitter** | RecursiveCharacterTextSplitter | Chunking |
| **Memory** | ConversationBufferMemory | Chat history |
| **UI (Local)** | Streamlit | Dark-themed web app |
| **UI (Deploy)** | Gradio | HuggingFace deployment |
| **PDF Export** | fpdf2 | Chat report generation |
| **Deployment** | HuggingFace Spaces | Cloud hosting |

---

## 📁 Project Structure

```
ResumeIQ-RAG-Chatbot/
│
├── 📂 Project/
│   ├── 🐍 resume_chatbot.py     ← Streamlit UI (local)
│   ├── 🐍 app.py                ← Gradio UI (HuggingFace)
│   ├── 📄 requirements.txt      ← Dependencies
│   └── 📂 faiss_index/          ← Saved vector store
│
├── 📂 Notebook/
│   └── 📓 Rag_langchain.ipynb   ← Development notebook
│
├── 📂 Data/
│   ├── 📄 Rahul01.pdf           ← Sample resume 1
│   └── 📄 Sonu_Jha_Resume.pdf   ← Sample resume 2
│
├── 📂 saved_resumes/            ← Saved resumes folder
├── 📂 saved_chats/              ← Saved chat PDFs
└── 📄 README.md
```

---

## 🔄 RAG Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG PIPELINE FLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📄 PDF/DOCX                                                 │
│      │                                                       │
│      ▼                                                       │
│  🧹 Text Cleaning  ──► Remove special chars, extra spaces    │
│      │                                                       │
│      ▼                                                       │
│  ✂️  Chunking  ──────► chunk_size=500, overlap=100           │
│      │                                                       │
│      ▼                                                       │
│  🔢 Embeddings  ────► OpenAI text-embedding-ada-002          │
│      │                                                       │
│      ▼                                                       │
│  🗄️  FAISS Store  ──► Vector similarity search               │
│      │                                                       │
│      ▼                                                       │
│  🔍 Retriever  ─────► k = all chunks (full context)          │
│      │                                                       │
│      ▼                                                       │
│  🤖 GPT-4o-mini  ───► Context + Question → Answer           │
│      │                                                       │
│      ▼                                                       │
│  💬 Chat Response + Memory (follow-up questions work)        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- OpenAI API Key → [Get here](https://platform.openai.com/api-keys)

### Step 1 — Clone Repository
```bash
git clone https://github.com/rahul07-github/ResumeIQ-RAG-Chatbot.git
cd ResumeIQ-RAG-Chatbot
```

### Step 2 — Create Virtual Environment
```bash
conda create -n resumeiq python=3.11
conda activate resumeiq
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run Streamlit App
```bash
cd Project
streamlit run resume_chatbot.py
```

### Step 5 — Open Browser
```
http://localhost:8501
```

---

## 🤗 HuggingFace Deployment

**Live App:** [https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot](https://huggingface.co/spaces/rahulkumarjha/ResumeIQ-Chatbot)

### How to Use Live Demo
1. Open the link above
2. Enter your **OpenAI API Key** in the sidebar (`sk-...`)
3. Upload any **PDF or DOCX** resume
4. Click **"⚡ Analyze Resume"**
5. Ask questions using text box or **Quick Question chips**
6. Click **"Save Chat as PDF"** to download the Q&A report

---

## ❌ Problems Faced & Solutions

This project had many real challenges — here is the complete honest journey:

---

### Problem 1 — Wrong Chunks Retrieved
```
Answer: "Not found in the document."
```
**Root Cause:** With k=5, the name chunk was never retrieved.
Resume had only 11 chunks — retriever was missing the header chunk.

**Solution:**
```python
# k = total number of chunks → retrieve everything
retriever = vectorstore.as_retriever(search_kwargs={"k": len(chunks)})
```

---

### Problem 2 — `tuple has no attribute page_content`
```
AttributeError: 'tuple' object has no attribute 'page_content'
```
**Root Cause:** PyMuPDF returned documents in wrong format.

**Solution:**
```python
from langchain_core.documents import Document
fixed_docs = [Document(page_content=d[0], metadata=d[1]) 
              for d in docs if isinstance(d, tuple)]
```

---

### Problem 3 — `No module named langchain.chains`
```
ModuleNotFoundError: No module named 'langchain.chains'
```
**Root Cause:** LangChain v1.2 removed ConversationalRetrievalChain.

**Solution:**
```bash
pip install langchain-classic
```
```python
from langchain_classic.chains import ConversationalRetrievalChain
```

---

### Problem 4 — GPU/RAM Crash (Ollama)
```
cudaMalloc failed: out of memory (status code: 500)
GGML_ASSERT(ctx->mem_buffer != NULL) failed
```
**Root Cause:** RTX 2050 (4GB VRAM) couldn't load llama3.2 with other apps running.

**Solution:** Switched to OpenAI API (cloud-based, no local GPU needed)
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
```

---

### Problem 5 — Gradio Version Conflicts (HuggingFace)
```
TypeError: Chatbot got unexpected argument 'bubble_full_width'
TypeError: Chatbot got unexpected argument 'type'
UserWarning: theme, css moved to launch()
```
**Root Cause:** HuggingFace kept installing latest Gradio — breaking changes in each version.

**Solution:** Pin exact version in requirements.txt
```txt
gradio==5.31.0
```

---

### Problem 6 — conda Not Recognized in PowerShell
```
'conda' is not recognized as a command
```
**Root Cause:** Conda PATH not set for PowerShell/CMD.

**Solution:**
```python
# Use sys.executable in notebook — always uses correct environment
import subprocess, sys
subprocess.Popen([sys.executable, "-m", "streamlit", "run", "resume_chatbot.py"])
```

---

### Problem 7 — Answer Format (One Long Paragraph)
**Root Cause:** LLM returned answers as one continuous paragraph.

**Solution:** Smart sentence splitter — split only at real sentence endings:
```python
import re
def format_answer(answer):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', answer.strip())
    return "\n\n".join(p.strip() for p in parts if p.strip())
```

---

## 💡 Key Learnings

- **RAG pipeline** is not just about LLM — the retriever quality matters most
- **Chunk size** must match document type — resumes need smaller chunks (300-500)
- **k = all chunks** is better for short documents like resumes
- **Local LLMs** are great but hardware-dependent — cloud APIs are more reliable for deployment
- **Version pinning** in requirements.txt is critical for stable deployments
- **"If it works, don't fix it"** — unnecessary changes cause more bugs

---

## 🔮 Future Improvements

- Multi-resume comparison (compare 2 resumes side by side)
- Candidate ranking system
- ATS score checker
- Export answers to Word document
- Support for image-based PDFs (OCR)
- Integration with LinkedIn profile

---

## 👨‍💻 Author

**Rahul Kumar Jha**
Data Analyst | ML Engineer | Fresher 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rahulkumarjha)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahul07-github)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-6c63ff?style=for-the-badge&logo=firefox&logoColor=white)](https://rahul07-github.github.io)

---

## 📜 License

```
COPYRIGHT © 2026 RAHUL KUMAR JHA. ALL RIGHTS RESERVED.

RESTRICTED LICENSE — VIEW ONLY

Permission is granted to VIEW and READ this source code for
educational and reference purposes ONLY.

The following are STRICTLY PROHIBITED without explicit written
permission from the author:

  ✗ Copying or reproducing any part of this code
  ✗ Modifying or creating derivative works
  ✗ Distributing or publishing this code
  ✗ Using this code for commercial purposes
  ✗ Submitting this code as your own work (academic or professional)

This project is part of the author's personal portfolio.
Unauthorized use will be considered a violation of intellectual
property rights.

For permissions or collaboration: rahulkumarjha9643@gmail.com
```

---

<div align="center">

**⭐ If you found this project helpful, please star the repository!**

*Built with ❤️ by Rahul Kumar Jha — Bhopal, India*

</div>
