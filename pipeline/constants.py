import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_API_URL=os.getenv("OLLAMA_API_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
  
LEETCODE_MASTER_PATH = "../leetcode-master"
OLLAMA_MODELS = ["llama2:13b", "gemma:insutrct", "mistral:instruct", "codellama:13b-code"]
OPENAI_MODELS = ["gpt-3.5-turbo-0125"]
ALLOWED_MODELS = OLLAMA_MODELS + OPENAI_MODELS