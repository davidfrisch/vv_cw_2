from LLM.BaseLLM import BaseLLM
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
class OpenAILLM(BaseLLM):
  def __init__(self, model):
      self.openai = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),
      )
      self.model = model
      
  def health_check(self):
      pass

  def predict(self, prompt, context=[]):
      completion = self.openai.chat.completions.create(
                                        messages = [
                                          {'role': 'system', 'content': 'You are a Java developer.'},
                                          {'role': 'user', 'content': prompt}], 
                                        model=self.model)
      
      reponse = completion.choices[0].message.content
      print(reponse)
      return reponse