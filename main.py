import base64
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    logger.error("GROQ_API_KEY is not set in the environment variables.")
    raise ValueError("GROQ_API_KEY is required but not set.")

def process_image(image_path, query):
    try:
        with open(image_path, "rb") as image_file:
            image_content = image_file.read()
            encoded_image = base64.b64encode(image_content).decode("utf-8")
         try: 
             img = Image.open(io.BytesIO(image_content))
         except Exception as e:
               logger.error (f"ivalid immage fermat : {str(e)}")
               return {"error": f"valid immage fermat: {str(e)}"}
            def make_api_request(model):
            response = requests.post(
                GROQ_API_URL, 
                json={
                    "model": model, 
                    "messages": messages, 
                    "max_tokens": 1000
                },
                headers = {
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout = 30
            )
            return response


    except Exception as e:
        logger.error(f"Invalid image format: {str(e)}")
        return {"error": f"Invalid image format: {str(e)}"}

if __name__ == "__main__":
    image_path = "test1.png"
    query = "What are the encoders in this picture?"
    result = process_image(image_path, query)
    print(result)
