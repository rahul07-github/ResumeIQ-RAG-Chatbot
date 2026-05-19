import streamlit as st
import os, re, tempfile
from datetime import datetime

st.set_page_config(
    page_title="ResumeIQ – AI Resume Chatbot",
    page_icon="🧠", layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg-main:    #0d0f14;
    --bg-card:    #13161e;
    --bg-hover:   #1a1e2a;
    --accent:     #6c63ff;
    --accent-2:   #00d4aa;
    --text-main:  #e8eaf0;
    --text-muted: #7a7f94;
    --border:     #252836;
    --user-bg:    #1e1b4b;
    --bot-bg:     #0d2118;
}

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif !important;
    background-color: var(--bg-main) !important;
    color: var(--text-main) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem !important; max-width: 1200px; }

[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border) !important;
}

/* ── Header ── */
.app-header {
    background: linear-gradient(135deg, #1a1040 0%, #0d1f18 50%, #1a0d2e 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    position: relative; overflow: hidden;
}
.app-header::before {
    content:''; position:absolute; top:-40px; right:-40px;
    width:200px; height:200px;
    background:radial-gradient(circle,rgba(108,99,255,.15) 0%,transparent 70%);
    border-radius:50%;
}
.header-title {
    font-size:2rem; font-weight:700;
    background:linear-gradient(90deg,#6c63ff,#00d4aa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text; margin:0 0 .3rem;
}
.header-sub { color:var(--text-muted); font-size:.9rem; margin:0; }

/* ── Status ── */
.status-badge {
    display:inline-flex; align-items:center; gap:6px;
    padding:4px 12px; border-radius:20px;
    font-size:.75rem; font-weight:500; margin-top:.8rem;
}
.status-ready   { background:rgba(0,212,170,.15); color:#00d4aa; border:1px solid rgba(0,212,170,.3); }
.status-waiting { background:rgba(255,107,107,.15); color:#ff6b6b; border:1px solid rgba(255,107,107,.3); }

/* ── Chat window ── */
.chat-wrap {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem;
    min-height: 400px; max-height: 520px;
    overflow-y: auto; margin-bottom: 1rem;
}
.chat-wrap::-webkit-scrollbar { width:4px; }
.chat-wrap::-webkit-scrollbar-thumb { background:var(--border); border-radius:4px; }

/* ── Bubbles ── */
.msg-row { display:flex; gap:10px; margin-bottom:1rem; align-items:flex-start; }
.msg-row.user { flex-direction:row-reverse; }
.avatar {
    width:34px; height:34px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:.8rem; font-weight:600; flex-shrink:0;
}
.avatar.user-av { background:linear-gradient(135deg,#6c63ff,#9b8fff); color:#fff; }
.avatar.bot-av  { background:linear-gradient(135deg,#00d4aa,#00a884); color:#0d1a17; }
.bubble {
    max-width:75%; padding:.75rem 1rem;
    border-radius:12px; font-size:.88rem; line-height:1.7;
    color: #e8eaf0 !important;          /* ✅ WHITE TEXT FIX */
}
.bubble p {
    color: #e8eaf0 !important;          /* ✅ WHITE TEXT FIX */
    margin:0 0 .5rem;
}
.bubble p:last-child { margin:0; }
.bubble.user {
    background:var(--user-bg);
    border:1px solid rgba(108,99,255,.35);
    border-top-right-radius:2px;
}
.bubble.bot {
    background:var(--bot-bg);
    border:1px solid rgba(0,212,170,.25);
    border-top-left-radius:2px;
}

/* ── Empty state ── */
.empty-state {
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    height:300px; color:var(--text-muted); gap:1rem;
}
.empty-icon { font-size:3rem; opacity:.4; }
.empty-text { font-size:.9rem; text-align:center; line-height:1.7; }

/* ── Input ── */
.stTextInput > div > div > input {
    background:var(--bg-card) !important;
    border:1px solid var(--border) !important;
    border-radius:10px !important;
    color:var(--text-main) !important;
    font-family:'Space Grotesk',sans-serif !important;
    padding:.7rem 1rem !important; font-size:.9rem !important;
}
.stTextInput > div > div > input:focus {
    border-color:var(--accent) !important;
    box-shadow:0 0 0 2px rgba(108,99,255,.2) !important;
}

/* ── Buttons ── */
.stButton > button {
    background:linear-gradient(135deg,var(--accent),#9b8fff) !important;
    color:#fff !important; border:none !important;
    border-radius:10px !important;
    font-family:'Space Grotesk',sans-serif !important;
    font-weight:500 !important;
}
.stButton > button:hover { opacity:.85 !important; }

/* ── Info card ── */
.info-card {
    background:var(--bg-hover); border:1px solid var(--border);
    border-radius:10px; padding:.8rem 1rem;
    margin-bottom:.8rem; font-size:.82rem; color:var(--text-muted);
}
.info-card strong { color:var(--text-main); }

/* ── Metrics ── */
.metrics-row { display:flex; gap:12px; margin-bottom:1rem; }
.metric-box {
    flex:1; background:var(--bg-card);
    border:1px solid var(--border);
    border-radius:10px; padding:.8rem; text-align:center;
}
.metric-val { font-size:1.4rem; font-weight:700; color:var(--accent-2,#00d4aa); }
.metric-lbl { font-size:.72rem; color:var(--text-muted); margin-top:2px; }

.divider { height:1px; background:var(--border); margin:1rem 0; }
.mono { font-family:'JetBrains Mono',monospace; font-size:.82rem; }
.sidebar-label {
    font-size:.72rem; font-weight:600; letter-spacing:.08em;
    text-transform:uppercase; color:var(--text-muted);
    margin-bottom:.5rem; padding-bottom:.3rem;
    border-bottom:1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)


# ── Session state ─────────────────────────────────────────────
for k, v in {
    "messages":[], "qa_chain":None, "file_name":None,
    "file_bytes":None, "file_ext":None,
    "chunks_count":0, "ready":False, "question_count":0,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── Helpers ───────────────────────────────────────────────────
def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    return re.sub(r'\s+',' ', text).strip()

def format_answer(answer):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', answer.strip())
    return "\n\n".join(p.strip() for p in parts if p.strip())

def process_file(uploaded_file):
    from langchain_ollama import ChatOllama, OllamaEmbeddings
    from langchain_community.document_loaders import PyMuPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import FAISS
    from langchain_classic.chains import ConversationalRetrievalChain
    from langchain_classic.memory import ConversationBufferMemory
    from langchain_core.prompts import PromptTemplate

    ext = "." + uploaded_file.name.split(".")[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if ext == ".pdf":
        loader = PyMuPDFLoader(tmp_path)
    else:
        from langchain_community.document_loaders import Docx2txtLoader
        loader = Docx2txtLoader(tmp_path)

    docs = loader.load()
    for doc in docs:
        doc.page_content = clean_text(doc.page_content)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embeddings  = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever   = vectorstore.as_retriever(search_kwargs={"k": len(chunks)})

    # llm    = ChatOllama(model="llama3.2", temperature=0,num_ctx=1024,num_gpu=0)
    llm    = ChatOllama(model="llama3.2", temperature=0,num_ctx=2048,num_gpu=1)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    prompt = PromptTemplate(
        input_variables=["context","question"],
        template="""Read the resume text below carefully and answer the question.
    Extract information directly from the text. Give a complete and specific answer.

Resume Context:
{context}

Question: {question}
Answer:"""
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        verbose=False
    )
    os.unlink(tmp_path)
    return qa_chain, len(chunks)


def save_resume():
    if st.session_state.file_bytes and st.session_state.file_name:
        os.makedirs("saved_resumes", exist_ok=True)
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"saved_resumes/{ts}_{st.session_state.file_name}"
        with open(path,"wb") as f:
            f.write(st.session_state.file_bytes)
        return path
    return None


def generate_chat_pdf():
    """Generate PDF of full chat Q&A session"""
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(70, 50, 200)
    pdf.cell(0, 12, "ResumeIQ - Chat Session Report", ln=True, align="C")

    # Date & file info
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(100, 100, 120)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True, align="C")
    if st.session_state.file_name:
        pdf.cell(0, 6, f"Resume: {st.session_state.file_name}", ln=True, align="C")
    pdf.ln(6)

    # Divider line
    pdf.set_draw_color(180, 180, 200)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(6)

    # Chat messages
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            # Question
            pdf.set_fill_color(230, 225, 255)
            pdf.set_text_color(40, 30, 120)
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 8, f"Q{(i//2)+1}: {msg['content']}", ln=True, fill=True)
            pdf.ln(2)
        else:
            # Answer
            pdf.set_text_color(20, 60, 40)
            pdf.set_font("Helvetica", "", 10)
            # Handle multiline answer
            clean = msg["content"].replace("\n\n", "\n").replace("\u2019","'").replace("\u2018","'")
            for char in ["\u201c","\u201d","\u2013","\u2014","\u2022"]:
                clean = clean.replace(char, "-")
            pdf.multi_cell(0, 7, f"Answer: {clean}")
            pdf.ln(4)

            # Separator
            pdf.set_draw_color(220, 220, 235)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(4)

    # Footer
    pdf.set_y(-20)
    pdf.set_font("Helvetica","I", 8)
    pdf.set_text_color(150,150,170)
    pdf.cell(0, 8, "Generated by ResumeIQ | Powered by LLaMA 3.2 + FAISS", align="C")

    # Save
    os.makedirs("saved_chats", exist_ok=True)
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"saved_chats/chat_{ts}.pdf"
    pdf.output(path)
    return path


# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-label">📄 Upload Resume</div>', unsafe_allow_html=True)

    uploaded = st.file_uploader("file", type=["pdf","docx"], label_visibility="collapsed")

    if uploaded:
        st.session_state.file_bytes = uploaded.getvalue()
        st.session_state.file_name  = uploaded.name
        st.session_state.file_ext   = uploaded.name.split(".")[-1].lower()

        if st.button("⚡ Analyze Resume", use_container_width=True):
            with st.spinner("Reading and indexing..."):
                try:
                    uploaded.seek(0)
                    qa, n = process_file(uploaded)
                    st.session_state.qa_chain       = qa
                    st.session_state.chunks_count   = n
                    st.session_state.ready          = True
                    st.session_state.messages       = []
                    st.session_state.question_count = 0
                    st.success("✅ Ready! Ask anything.")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.session_state.file_name:
        st.markdown(f"""
        <div class="info-card">
            <strong>📁 File:</strong><br>
            <span class="mono">{st.session_state.file_name}</span><br><br>
            <strong>Chunks:</strong> {st.session_state.chunks_count} &nbsp;|&nbsp;
            <strong>Q&A:</strong> {st.session_state.question_count}
        </div>
        """, unsafe_allow_html=True)

    # ── Save Resume ──
    if st.session_state.ready:
        st.markdown('<div class="sidebar-label">💾 Save Resume</div>', unsafe_allow_html=True)
        if st.button("Save Resume to Disk", use_container_width=True):
            path = save_resume()
            st.success(f"✅ Saved!\n`{path}`") if path else st.error("Nothing to save.")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Save Chat as PDF ── ✅ NEW FEATURE
    if st.session_state.messages:
        st.markdown('<div class="sidebar-label">📥 Save Chat</div>', unsafe_allow_html=True)

        if st.button("💬 Save Chat as PDF", use_container_width=True):
            try:
                import fpdf
                path = generate_chat_pdf()
                st.success(f"✅ Chat saved!\n`{path}`")

                # Download button
                with open(path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=f.read(),
                        file_name=os.path.basename(path),
                        mime="application/pdf",
                        use_container_width=True
                    )
            except ImportError:
                st.error("Run: pip install fpdf2")

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Clear ──
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.question_count = 0
            st.rerun()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:.75rem;color:#7a7f94;line-height:1.9;">
        🧠 <strong style="color:#e8eaf0">ResumeIQ</strong><br>
        Powered by LLaMA 3.2 + FAISS<br>
        🔒 Local · Private · Fast
    </div>
    """, unsafe_allow_html=True)


# ── Main ──────────────────────────────────────────────────────
status_cls  = "status-ready"   if st.session_state.ready else "status-waiting"
status_text = "● Resume Ready" if st.session_state.ready else "● No Resume Loaded"

st.markdown(f"""
<div class="app-header">
    <div class="header-title">🧠 ResumeIQ</div>
    <p class="header-sub">AI-powered resume analysis — upload any resume, ask anything instantly.</p>
    <span class="status-badge {status_cls}">{status_text}</span>
</div>
""", unsafe_allow_html=True)

# Metrics
if st.session_state.ready:
    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-box">
            <div class="metric-val">{st.session_state.chunks_count}</div>
            <div class="metric-lbl">Chunks Indexed</div>
        </div>
        <div class="metric-box">
            <div class="metric-val">{st.session_state.question_count}</div>
            <div class="metric-lbl">Questions Asked</div>
        </div>
        <div class="metric-box">
            <div class="metric-val">{len(st.session_state.messages)}</div>
            <div class="metric-lbl">Total Messages</div>
        </div>
        <div class="metric-box">
            <div class="metric-val">{st.session_state.file_ext.upper()}</div>
            <div class="metric-lbl">File Format</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick chips
CHIPS = [
    "Who is this person?","What are the skills?",
    "Tell me about internship","What projects were built?",
    "What is the GPA?","Education background?",
]
if st.session_state.ready:
    st.markdown("**💡 Quick Questions**")
    cols = st.columns(3)
    for i, chip in enumerate(CHIPS):
        with cols[i % 3]:
            if st.button(chip, key=f"chip_{i}", use_container_width=True):
                st.session_state["_pending"] = chip

# ── Chat window ───────────────────────────────────────────────
chat_html = '<div class="chat-wrap">'
if not st.session_state.messages:
    chat_html += """
    <div class="empty-state">
        <div class="empty-icon">💬</div>
        <div class="empty-text">Upload a resume from the sidebar<br>then start asking questions.</div>
    </div>"""
else:
    for msg in st.session_state.messages:
        content = (msg["content"]
                   .replace("&","&amp;")
                   .replace("<","&lt;")
                   .replace(">","&gt;"))
        if msg["role"] == "user":
            chat_html += f"""
            <div class="msg-row user">
                <div class="avatar user-av">You</div>
                <div class="bubble user"><p>{content}</p></div>
            </div>"""
        else:
            fmt = content.replace("\n\n","</p><p>").replace("\n","<br>")
            chat_html += f"""
            <div class="msg-row bot">
                <div class="avatar bot-av">AI</div>
                <div class="bubble bot"><p>{fmt}</p></div>
            </div>"""
chat_html += "</div>"
st.markdown(chat_html, unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────
col1, col2 = st.columns([5,1])
with col1:
    user_q = st.text_input(
        "q", placeholder="Ask anything about the resume...",
        label_visibility="collapsed", key="q_input"
    )
with col2:
    send = st.button("Send →", use_container_width=True)

if "_pending" in st.session_state:
    user_q = st.session_state.pop("_pending")
    send   = True

# ── Process ───────────────────────────────────────────────────
if send and user_q.strip():
    if not st.session_state.ready:
        st.warning("⚠️ Please upload and analyze a resume first!")
    else:
        st.session_state.messages.append({"role":"user","content":user_q.strip()})
        with st.spinner("Thinking..."):
            try:
                res    = st.session_state.qa_chain.invoke({"question":user_q.strip()})
                answer = format_answer(res["answer"])
                st.session_state.messages.append({"role":"assistant","content":answer})
                st.session_state.question_count += 1
            except Exception as e:
                st.session_state.messages.append({"role":"assistant","content":f"Error: {e}"})
        st.rerun()
