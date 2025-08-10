import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    HF_TOKEN = os.getenv("HF_TOKEN")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    HUGGINFACEHUB_API_TOKEN = os.getenv("HUGGINFACEHUB_API_TOKEN")
    HFEmbeddings="sentence-transformers/all-MiniLM-L6-v2"
    HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
    data = "data/"
    vector_database = "vector_store/faiss_db"
    chunk_size = 500
    chunk_overlap = 50
    model_name = "gemini-2.5-pro"

config = Config()

