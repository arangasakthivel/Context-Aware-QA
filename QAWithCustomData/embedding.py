import sys
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.prompts import PromptTemplate

from exception import customexception
from logger import logging


CUSTOM_QA_PROMPT = PromptTemplate(
"""
You are a document question-answering assistant.

RULES:
- Use ONLY the information present in the document.
- You may combine information from multiple parts of the document.
- Do NOT use external knowledge.
- If the document truly does not address the question, say:
  "The document does not contain information about this."
- Write in short, clear paragraphs.
- Use bullet points where helpful.

Question:
{query_str}

Answer:
"""
)

def download_genai_embedding(documents):
    """
    Create vector embeddings using Gemini Embedding model
    and return a query engine.
    """
    try:
        logging.info("Initializing Gemini embedding model")

        # Prevent LlamaIndex from defaulting to OpenAI
        # Settings.llm = None

        # Gemini embedding model (same as rest of project)
        Settings.embed_model = GeminiEmbedding(
            model="gemini-embedding-001"
        )

        logging.info("Creating vector index")
        index = VectorStoreIndex.from_documents(documents)

        # Persist index to disk (VERY important)
        index.storage_context.persist()

        logging.info("Creating query engine")
        query_engine = index.as_query_engine(
            similarity_top_k=4,
            response_mode="compact",

        )

        return query_engine

    except Exception as e:
        logging.error("Exception occurred during embedding generation")
        raise customexception(e, sys)
