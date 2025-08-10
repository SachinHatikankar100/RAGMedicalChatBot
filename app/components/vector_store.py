from components.pdf_loader import create_text_chunks
from common.custom_exception import CustomException
from common.logger import get_logger
from components.embedding import embedding
from langchain_community.vectorstores import FAISS
from config.config import Config
import os

logger = get_logger(__name__)

def load_vector_store():
    try:
        hfembedding = embedding()
        if os.path.exists(Config.vector_database):
            return FAISS.load_local(
                Config.vector_database,
                hfembedding,
                allow_dangerous_deserialization=True

            )
        else:
            logger.error("No vectore store found...")


    except Exception as e:
        raise CustomException("loading vector failed")


def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise Exception("No chunks found")
        
        hfembedding = embedding()
        db = FAISS.from_documents(hfembedding,text_chunks)

        db.save_local(Config.vector_database)

        return db

    except Exception as e:
        raise CustomException("saving vector failed")
    
