import random
import gradio as gr
import requests
from app.components.retriever import get_answer
from app.common.custom_exception import CustomException
from app.common.logger import get_logger

logger = get_logger(__name__)


def medical_response(message, history):
    try:
        response = get_answer(message)
        return response
    except Exception as e:
        error_message = CustomException("Error while getting response from retriever",e)
        raise error_message


demo = gr.ChatInterface(
    medical_response, 
    type="messages", 
    submit_btn="Send Medical Query",
    autofocus=False)
demo.launch()