# 📄 Question–Answering Application built with LlamaIndex and Google Gemini

A **context-aware Question Answering (QA) system** that enables users to upload documents and ask natural-language questions.  
The system generates answers **strictly from the uploaded document content**, without using external knowledge.

Built using **LlamaIndex**, **Google Gemini**, and **Streamlit**, with a modern ChatGPT-style user interface.

🔗 **Live Application**  
👉 https://context-aware-app-c5th6rfq5caj7cntkrwvrw.streamlit.app/

---

## 🚀 Features

- 📂 Upload documents in multiple formats:
  - PDF (including scanned PDFs with OCR)
  - TXT
  - DOCX
  - CSV
  - HTML
- 🧠 Context-aware answers using vector embeddings
- 🚫 No hallucinations — answers are generated only from document content
- 🔍 Automatic OCR fallback for scanned PDFs
- ✨ Clean, ChatGPT-style conversational UI
- ☁️ Deployed on Streamlit Cloud

---

## 🧩 System Architecture

📌 *(Insert architecture diagram image here)*

**High-level flow:**
1. User uploads a document  
2. Text is extracted (OCR if required)  
3. Document is split into semantic chunks  
4. Vector embeddings are created using Gemini Embeddings  
5. Query is matched against document vectors  
6. Gemini LLM generates a context-aware response  

---

## 🛠️ Tech Stack

### Frontend
- Streamlit  
- Custom CSS (ChatGPT-style UI)

### Backend / AI
- LlamaIndex – document indexing & retrieval  
- Google Gemini – large language model  
- Gemini Embeddings – vector representation  
- PyPDF2 / pdf2image / pytesseract – document parsing & OCR  

### Deployment
- Streamlit Cloud

---

## 📂 Project Structure

```text
.
├── StreamlitApp.py
├── QAWithCustomData
│   ├── data_ingestion.py
│   ├── embedding.py
│   ├── model_api.py
│   ├── logger.py
│   └── exception.py
├── requirements.txt
└── README.md
