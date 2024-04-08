import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_API_URL=os.getenv("OLLAMA_API_URL")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
CONTAINERS_TYPE=os.getenv("CONTAINERS_TYPE")

if CONTAINERS_TYPE is None:
    raise Exception("CONTAINERS_TYPE is not set, please set it to 'docker' or 'singularity'")
  
  
LEETCODE_MASTER_PATH = "../leetcode-master"
OLLAMA_MODELS = ["llama2:13b", "gemma:insutrct", "mistral:instruct", "deepseek-coder:6.7b-instruct"]
OPENAI_MODELS = ["gpt-3.5-turbo-0125"]
ALLOWED_MODELS = OLLAMA_MODELS + OPENAI_MODELS