from setuptools import find_packages, setup

setup(
    name="QAApplication_LlamaIndex_GoogleGenAI",
    version="0.0.1",
    author="Aranga Sakthivel R",
    author_email="aranga567@gmail.com",
    description="Question Answering application using LlamaIndex and Google Gemini",
    packages=find_packages(),
    install_requires=[
        "llama-index",
        "google-generativeai",
        "llama-index-llms-gemini",
        "llama-index-embeddings-gemini",
        "python-dotenv",
        "streamlit",
        "PyPDF2",
        "python-docx",
        "pandas",
        "beautifulsoup4",
        "IPython",
    ],
)
