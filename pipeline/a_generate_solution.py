import requests
import json
from constants import OLLAMA_API_URL



def generate_solution(prompt, context, model):
    r = requests.post(f'{OLLAMA_API_URL}/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      })
    
    r.raise_for_status()

    model_response = ""
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        model_response += response_part

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context'], model_response
          
          
      
    