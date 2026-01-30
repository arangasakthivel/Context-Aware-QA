import os
import sys
from dotenv import load_dotenv

import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings

from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set")

# Configure Gemini SDK
genai.configure(api_key=GOOGLE_API_KEY)


def load_model():
    """
    Loads a Gemini LLM for response generation.

    Returns:
    - Gemini: Configured Gemini LLM instance
    """
    try:
        logging.info("Loading Gemini LLM...")

        # ✅ Correct LLM class
        llm = Gemini(
            model="models/gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

        # ✅ Correct global registration (LlamaIndex ≥ 0.14)
        Settings.llm = llm

        logging.info("Gemini LLM loaded successfully")
        return llm

    except Exception as e:
        logging.error("Error loading Gemini model")
        raise customexception(e, sys)
