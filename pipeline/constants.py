import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

if not OLLAMA_API_URL:
    raise Exception("OLLAMA_API_URL is not set in the environment variables.")
if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY is not set in the environment variables.")
  
LEETCODE_MASTER_PATH = "../leetcode-master"
OLLAMA_MODELS = ["llama2:latest", "gemma"]
OPENAI_MODELS = ["gpt-3.5-turbo-0125"]
ALLOWED_MODELS = OLLAMA_MODELS + OPENAI_MODELS