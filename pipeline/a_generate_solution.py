import requests
import json
from constants import OLLAMA_API_URL



OLLAMA_MODELS = ["llama2:latest", "gemma"]
OPENAI_MODELS = ["gpt-3.5-turbo-0125"]

def generate_solution(prompt, context, model):
    llm = None
    if model in OPENAI_MODELS:
        from LLM.OpenAILLM import OpenAILLM
        print("OpenAI")
        llm = OpenAILLM(model)
    elif model in OLLAMA_MODELS:
        from LLM.OllamaLLM import OllamaAI
        print("Ollama")
        llm = OllamaAI(OLLAMA_API_URL, model)
    else:
        raise Exception(f"Model {model} not supported")
      
    llm.health_check()
    return context, llm.predict(prompt, context)
          
          
      
    