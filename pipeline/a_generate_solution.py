import requests
import json
from constants import OLLAMA_API_URL, OPENAI_MODELS, OLLAMA_MODELS


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
          
          
      
    