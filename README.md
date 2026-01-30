# 📄 Question–Answering Application built with LlamaIndex and Google Gemini

A **context-aware Question Answering (QA) system** that enables users to upload documents and ask natural-language questions.  
The system generates answers **strictly from the uploaded document content**, without using external knowledge.

Built using **LlamaIndex**, **Google Gemini**, and **Streamlit**, with a modern ChatGPT-style user interface.

🔗 **Live Application**  
👉 https://context-aware-app-c5th6rfq5caj7cntkrwvrw.streamlit.app/

---

## 🧩 System Architecture

![Adobe Scan 30 Jan 2026_page-0001](https://github.com/user-attachments/assets/0d3abdda-69a3-4836-8633-672790af1a51)


**High-level flow:**
1. User uploads a document  
2. Text is extracted  
3. Document is split into semantic chunks  
4. Vector embeddings are created using Gemini Embeddings  
5. Query is matched against document vectors  
6. Gemini LLM generates a context-aware response
   

---

## 🚀 Features

- 📂 Upload documents in multiple formats:
  - PDF
  - TXT
  - DOCX
  - CSV
  - HTML
- 🧠 Context-aware answers using vector embeddings
- 🚫 No hallucinations — answers are generated only from document content
- ✨ Clean, ChatGPT-style conversational UI
- ☁️ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

### Frontend
- Streamlit  
- Custom CSS (ChatGPT-style UI)

### Backend / AI
- LlamaIndex – document indexing & retrieval  
- Google Gemini – large language model  
- Gemini Embeddings – vector representation  
- PyPDF2 / pdf2image / pytesseract – document parsing 

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
| TXT                | UTF-8 decoding                      |
| DOCX               | python-docx                         |
| CSV                | pandas                              |
| HTML               | BeautifulSoup                       |

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/context-aware-qa.git
cd context-aware-qa
```

### 2️⃣ Create and activate a virtual environment
```bash
conda create -n qa-app python=3.10
conda activate qa-app
```

> You can also use `venv` if you prefer:
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables
Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 5️⃣ Run the application
```bash
streamlit run StreamlitApp.py
```

## 🧠 How It Works

### Data Ingestion
- Extracts text from uploaded documents
- Normalizes and chunks content

### Embedding Generation
- Each chunk is converted into vector embeddings
- Stored using LlamaIndex’s vector store

### Query Processing
- User query is embedded
- Most relevant document chunks are retrieved

### Response Generation
- Gemini LLM generates an answer using only retrieved context
- Output is formatted for readability

---

## 🧪 Example Use Cases

- Academic document summarization
- Policy or legal document Q&A
- Project reports & research papers
- Interview preparation from notes
- Government forms or scanned PDFs

---

## 🔐 Limitations

- Requires internet connectivity for Gemini API
- Very large documents may take longer to process

---

## 🖼️ Screenshots

<img width="1397" height="719" alt="Screenshot 2026-01-30 at 2 32 11 AM" src="https://github.com/user-attachments/assets/5e549d53-b6a3-4516-88ba-9a5a273e9c41" />


<img width="1397" height="719" alt="Screenshot 2026-01-30 at 2 33 17 AM" src="https://github.com/user-attachments/assets/a8fe20d1-195e-487b-ba33-1fe543bdd715" />


<img width="1397" height="719" alt="Screenshot 2026-01-30 at 2 35 44 AM" src="https://github.com/user-attachments/assets/b3b0ae5e-662f-4735-b7fb-2cc356558f7c" />


<img width="1395" height="691" alt="Screenshot 2026-01-30 at 2 36 14 AM" src="https://github.com/user-attachments/assets/ee01435e-38e3-4301-a7f8-0cdf4bed62d5" />


---

## 📈 Future Enhancements

- Multi-document chat support
- Conversation memory across queries
- Highlight source paragraphs
- Multilingual and querying
- Export answers as PDF

---

## 👨‍💻 Author

**Aranga Sakthivel R**  
B.Tech – Information Technology  
VIT Vellore

---

## 📜 License

This project is intended for **educational and academic use**.  
You may extend or modify it with proper attribution.

