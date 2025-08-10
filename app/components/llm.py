from langchain_google_genai import ChatGoogleGenerativeAI
from common.custom_exception import CustomException
from common.logger import get_logger
from config.config import Config

logger = get_logger(__name__)

def load_llm(model_name:str = Config.model_name, gemini_api_key:str = Config.GOOGLE_API_KEY):
    try:
        logger.info("loading llm started")

        llm = ChatGoogleGenerativeAI(
            model= model_name,
            gemini_api_key = gemini_api_key,
            temperature=0.3,
            max_tokens=256
        )
        logger.info("loading llm completed")
        return llm
    except Exception as e:
        error_message = CustomException("Failed while loading LLM",e)
        logger.error(str(error_message))