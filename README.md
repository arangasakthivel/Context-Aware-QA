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
```
## 📥 Supported File Processing

| File Type           | Method Used                         |
|--------------------|-------------------------------------|
| PDF (text-based)   | PyPDF2                              |
| PDF (scanned)      | OCR (Tesseract + pdf2image)         |
| TXT                | UTF-8 decoding                      |
| DOCX               | python-docx                         |
| CSV                | pandas                              |
| HTML               | BeautifulSoup                       |

⚙️ Installation & Setup (Local)
1️⃣ Clone the repository
git clone https://github.com/your-username/context-aware-qa.git
cd context-aware-qa

2️⃣ Create and activate virtual environment
conda create -n qa-app python=3.10
conda activate qa-app

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

GOOGLE_API_KEY=your_google_gemini_api_key

5️⃣ Run the application
streamlit run StreamlitApp.py

🧠 How It Works
Data Ingestion

Extracts text from uploaded documents

Applies OCR if text is missing or garbled

Normalizes and chunks content

Embedding Generation

Each chunk is converted into vector embeddings

Stored using LlamaIndex’s vector store

Query Processing

User query is embedded

Most relevant document chunks are retrieved

Response Generation

Gemini LLM generates an answer using only retrieved context

Output is formatted for readability

🧪 Example Use Cases

Academic document summarization

Policy or legal document Q&A

Project reports & research papers

Interview preparation from notes

Government forms or scanned PDFs

🔐 Limitations

Requires internet connectivity for Gemini API

OCR accuracy depends on scan quality

Very large documents may take longer to process

🖼️ Screenshots

📌 (Insert Streamlit UI screenshots here)

📈 Future Enhancements

Multi-document chat support

Conversation memory across queries

Highlight source paragraphs

Multilingual OCR and querying

Export answers as PDF

👨‍💻 Author

Aranga Sakthivel R
B.Tech – Information Technology
VIT Vellore

📜 License

This project is intended for educational and academic use.
You may extend or modify it with proper attribution.
