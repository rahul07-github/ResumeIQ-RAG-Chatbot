import gradio as gr
import os, re, tempfile
from datetime import datetime

qa_chain_global = None
file_info = {"name": None, "bytes": None, "chunks": 0}

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def format_answer(answer):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', answer.strip())
    return "\n\n".join(p.strip() for p in parts if p.strip())

def analyze_resume(file, api_key):
    global qa_chain_global, file_info
    if file is None:
        return [], "*⚠️ Please upload a resume file.*", "● No File Loaded"
    if not api_key or not api_key.startswith("sk-"):
        return [], "*⚠️ Please enter a valid OpenAI API key.*", "● No API Key"
    try:
        from langchain_openai import ChatOpenAI, OpenAIEmbeddings
        from langchain_community.document_loaders import PyMuPDFLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from langchain_community.vectorstores import FAISS
        from langchain_classic.chains import ConversationalRetrievalChain
        from langchain_classic.memory import ConversationBufferMemory
        from langchain_core.prompts import PromptTemplate

        ext = os.path.splitext(file.name)[1].lower()
        if ext == ".pdf":
            loader = PyMuPDFLoader(file.name)
        else:
            from langchain_community.document_loaders import Docx2txtLoader
            loader = Docx2txtLoader(file.name)

        docs = loader.load()
        for doc in docs:
            doc.page_content = clean_text(doc.page_content)

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = splitter.split_documents(docs)

        embeddings  = OpenAIEmbeddings(api_key=api_key)
        vectorstore = FAISS.from_documents(chunks, embeddings)
        retriever   = vectorstore.as_retriever(search_kwargs={"k": len(chunks)})

        llm    = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""You are a professional resume analyst.
Read the resume carefully and answer the question directly.
Extract exact information from the resume text.

Resume:
{context}

Question: {question}
Answer:"""
        )
        qa_chain_global = ConversationalRetrievalChain.from_llm(
            llm=llm, retriever=retriever, memory=memory,
            combine_docs_chain_kwargs={"prompt": prompt},
            verbose=False
        )

        with open(file.name, "rb") as f:
            file_info["bytes"] = f.read()
        file_info["name"]   = os.path.basename(file.name)
        file_info["chunks"] = len(chunks)

        info = (
            f"**📁 File:** {file_info['name']}\n\n"
            f"**📦 Chunks:** {len(chunks)}\n\n"
            f"**📄 Pages:** {len(docs)}\n\n"
            f"**✅ Status:** Ready!"
        )
        return [], info, "● Resume Ready ✅"

    except Exception as e:
        return [], f"**❌ Error:** {str(e)}", "● Error"


def ask_question(question, history, api_key):
    global qa_chain_global
    if not question.strip():
        return history, ""
    if not api_key or not api_key.startswith("sk-"):
        return history + [
            {"role": "user",      "content": question},
            {"role": "assistant", "content": "⚠️ Please enter OpenAI API key first!"}
        ], ""
    if qa_chain_global is None:
        return history + [
            {"role": "user",      "content": question},
            {"role": "assistant", "content": "⚠️ Please upload and analyze a resume first!"}
        ], ""
    try:
        result = qa_chain_global.invoke({"question": question.strip()})
        answer = format_answer(result["answer"])
        return history + [
            {"role": "user",      "content": question.strip()},
            {"role": "assistant", "content": answer}
        ], ""
    except Exception as e:
        return history + [
            {"role": "user",      "content": question.strip()},
            {"role": "assistant", "content": f"❌ Error: {str(e)}"}
        ], ""


def save_chat(history):
    if not history:
        return "⚠️ No chat to save."
    try:
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(70, 50, 200)
        pdf.cell(0, 12, "ResumeIQ - Chat Session", ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(120, 120, 140)
        pdf.cell(0, 8, f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}", ln=True, align="C")
        if file_info["name"]:
            pdf.cell(0, 6, f"Resume: {file_info['name']}", ln=True, align="C")
        pdf.ln(5)

        q_num = 1
        for msg in history:
            role    = msg.get("role", "")
            content = msg.get("content", "")
            if role == "user":
                pdf.set_fill_color(230, 225, 255)
                pdf.set_text_color(40, 30, 120)
                pdf.set_font("Helvetica", "B", 10)
                clean_q = str(content).encode('latin-1','replace').decode('latin-1')
                pdf.cell(0, 8, f"Q{q_num}: {clean_q}", ln=True, fill=True)
                pdf.ln(2)
                q_num += 1
            else:
                pdf.set_text_color(20, 60, 40)
                pdf.set_font("Helvetica", "", 10)
                clean_a = str(content).replace("\n\n", "\n")
                for ch in ["\u2019","\u2018","\u201c","\u201d","\u2013","\u2014","\u2022"]:
                    clean_a = clean_a.replace(ch, "-")
                clean_a = clean_a.encode('latin-1','replace').decode('latin-1')
                pdf.multi_cell(0, 7, f"Answer: {clean_a}")
                pdf.ln(3)

        os.makedirs("saved_chats", exist_ok=True)
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"saved_chats/chat_{ts}.pdf"
        pdf.output(path)
        return f"✅ Chat saved → {path}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


def clear_all():
    global qa_chain_global, file_info
    qa_chain_global = None
    file_info = {"name": None, "bytes": None, "chunks": 0}
    return [], "*Upload a resume to get started.*", "● No File Loaded"


CHIPS = [
    "Who is this person?",
    "What are the technical skills?",
    "Tell me about internship",
    "What projects were built?",
    "What is the GPA?",
    "Education background?",
    "What certifications does he have?",
    "Summarize this resume",
]

with gr.Blocks(title="ResumeIQ — AI Resume Chatbot") as demo:

    gr.Markdown("""
    # 🧠 ResumeIQ — AI Resume Chatbot
    > AI-powered resume analysis — Upload any resume, ask anything instantly.
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🔑 OpenAI API Key")
            api_key_box = gr.Textbox(placeholder="sk-...", type="password", show_label=False)

            gr.Markdown("### 📄 Upload Resume")
            file_input  = gr.File(file_types=[".pdf", ".docx"], label="PDF or DOCX")
            analyze_btn = gr.Button("⚡ Analyze Resume", variant="primary")
            status_box  = gr.Textbox(value="● No File Loaded", label="Status", interactive=False)

            gr.Markdown("### 📋 File Info")
            file_info_box = gr.Markdown("*Upload a resume to get started.*")

            gr.Markdown("### 💾 Save Chat")
            save_btn = gr.Button("Save Chat as PDF", variant="secondary")
            save_out = gr.Textbox(show_label=False, interactive=False)

            clear_btn = gr.Button("🗑️ Clear All", variant="stop")

            gr.Markdown("""
            ---
            🧠 **ResumeIQ** | GPT-4o-mini + FAISS + LangChain
            🔒 API key is never stored
            """)

        with gr.Column(scale=3):
            gr.Markdown("### 💡 Quick Questions")
            with gr.Row():
                chip_btns = []
                for chip in CHIPS[:4]:
                    b = gr.Button(chip, size="sm")
                    chip_btns.append(b)
            with gr.Row():
                for chip in CHIPS[4:]:
                    b = gr.Button(chip, size="sm")
                    chip_btns.append(b)

            chatbot = gr.Chatbot(
                label="Chat",
                height=450,
                show_label=False,
                type="messages"
                )

            with gr.Row():
                question_box = gr.Textbox(
                    placeholder="Ask anything about the resume...",
                    show_label=False, scale=5
                )
                send_btn = gr.Button("Send →", variant="primary", scale=1)

    # Events
    analyze_btn.click(
        fn=analyze_resume,
        inputs=[file_input, api_key_box],
        outputs=[chatbot, file_info_box, status_box]
    )
    send_btn.click(
        fn=ask_question,
        inputs=[question_box, chatbot, api_key_box],
        outputs=[chatbot, question_box]
    )
    question_box.submit(
        fn=ask_question,
        inputs=[question_box, chatbot, api_key_box],
        outputs=[chatbot, question_box]
    )
    save_btn.click(fn=save_chat, inputs=[chatbot], outputs=[save_out])
    clear_btn.click(fn=clear_all, outputs=[chatbot, file_info_box, status_box])

    for btn, chip_text in zip(chip_btns, CHIPS):
        btn.click(fn=lambda t=chip_text: t, outputs=[question_box])

if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Soft(
            primary_hue="violet",
            secondary_hue="emerald",
            neutral_hue="slate"
        )
    )
