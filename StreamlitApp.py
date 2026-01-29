import streamlit as st
import re

from QAWithCustomData.data_ingestion import load_data
from QAWithCustomData.embedding import download_genai_embedding
from QAWithCustomData.model_api import load_model


# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Document QA",
    page_icon="📄",
    layout="wide"
)


# ----------------- GLOBAL CSS -----------------
st.markdown("""
<style>

/* ===== ROOT APP ===== */
.stApp {
    background: radial-gradient(circle at top, #0f172a 0%, #020617 60%);
    color: #e5e7eb;
}

/* ===== WIDTH ===== */
.block-container {
    max-width: 1400px;
    padding-top: 2.5rem;
}

/* ===== LEFT PANEL ===== */
.doc-panel {
    background: #020617;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* ===== USER BUBBLE ===== */
.user-bubble {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    padding: 10px 14px;
    border-radius: 14px;
    font-size: 14px;
    margin: 12px 0;
    margin-left: auto;
    max-width: 75%;
}

/* ===== ASSISTANT BUBBLE ===== */
.assistant-bubble {
    background: #111827;
    color: #e5e7eb;
    padding: 16px 18px;
    border-radius: 14px;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 20px;
    max-width: 85%;
}

/* ===== TEXT SPACING ===== */
.assistant-bubble p { margin: 0 0 0.6rem; }
.assistant-bubble li { margin-bottom: 0.3rem; }

/* ===== INPUTS ===== */
input, textarea {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 10px !important;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1.4rem;
    font-weight: 500;
}

/* ===== REMOVE STREAMLIT CHROME ===== */
footer, header { visibility: hidden; }

</style>
""", unsafe_allow_html=True)


# ----------------- CLEAN OUTPUT -----------------
def clean_markdown(text: str) -> str:
    text = re.sub(r"\*{3,}", "", text)
    text = re.sub(r"\*{2}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ----------------- SESSION STATE -----------------
if "query_engine" not in st.session_state:
    st.session_state.query_engine = None

if "chat" not in st.session_state:
    st.session_state.chat = []


# ----------------- APP -----------------
def main():

    # ---------- HEADER ----------
    st.markdown(
        "<h2 style='text-align:center;'>📄 Document Question Answering</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#9ca3af;'>Chat with your document using LlamaIndex + Gemini</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # ---------- SPLIT SCREEN ----------
    left, right = st.columns([1, 2], gap="large")

    # ---------- LEFT: DOCUMENT PANEL ----------
    with left:

        st.markdown("### 📎 Document")

        uploaded_file = st.file_uploader(
            "Upload a document",
            type=["pdf", "txt", "docx", "csv", "html"]
        )

        if uploaded_file:
            st.success("Document uploaded")

            st.markdown("**Filename**")
            st.code(uploaded_file.name)

            if st.button("📥 Load Document"):
                with st.spinner("Processing document..."):
                    documents = load_data(uploaded_file)
                    load_model()
                    st.session_state.query_engine = download_genai_embedding(documents)
                    st.session_state.chat = []

                st.success("Document ready to chat")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------- RIGHT: CHAT PANEL ----------
    with right:
        st.markdown("### 💬 Ask Questions")

        if st.session_state.query_engine is None:
            st.info("Upload and load a document to start chatting.")
        else:
            user_question = st.text_input(
                "Your question",
                placeholder="e.g. Give me a summary of this document"
            )

            if st.button("Ask") and user_question.strip():
                with st.spinner("Thinking..."):
                    response = st.session_state.query_engine.query(user_question)
                    answer = clean_markdown(response.response)

                st.session_state.chat.append(("user", user_question))
                st.session_state.chat.append(("assistant", answer))

            # ---------- CHAT HISTORY ----------
            for role, msg in st.session_state.chat:
                if role == "user":
                    st.markdown(
                        f"<div class='user-bubble'><b>You:</b> {msg}</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<div class='assistant-bubble'>{msg.replace(chr(10), '<br>')}</div>",
                        unsafe_allow_html=True
                    )


if __name__ == "__main__":
    main()
