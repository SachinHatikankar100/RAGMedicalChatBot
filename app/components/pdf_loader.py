from common.custom_exception import CustomException
from common.logger import get_logger
import os
from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.config import Config
logger = get_logger(__name__)

def load_pdf():
    try:
        if not os.path.exists(Config.data):
            raise CustomException("File path does not exists")
        
        loader = DirectoryLoader(Config.data,glob="*.pdf",loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            raise CustomException("No documents found")
        
        return documents

    except:
        raise CustomException("Data path not found")


def create_text_chunks(documents):
    try:
        if not documents:
            raise Exception("No documents found")
        
        text_splitter = RecursiveCharacterTextSplitter(Config.chunk_size, Config.chunk_overlap)
        text_chunks = text_splitter.split_documents(documents)

        return text_chunks
    except:
        raise CustomException("Chunking failed")