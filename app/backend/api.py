from typing import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.common.custom_exception import CustomException
from app.common.logger import get_logger
from app.components.retriever import retrieve_qa_chain,get_answer

logger = get_logger(__name__)

app = FastAPI()


