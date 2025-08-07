import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    HF_TOKEN = os.getenv("HF_TOKEN")
    HUGGINFACEHUB_API_TOKEN = os.getenv("HUGGINFACEHUB_API_TOKEN")
    HUGGINGFACE_REPO_ID = "NeuML/bioclinical-modernbert-base-embeddings"
    data = "data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf"
    vector_database = "vector/faiss_db"
    chunk_size = 500
    chunk_overlap = 50

config = Config()

