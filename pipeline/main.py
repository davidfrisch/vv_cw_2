from a_generate_solution import generate_solution
from b_extract_and_insert import extract_and_insert
# from c_compile_and_verify import feedback
# from d_feedback import a_feedback
from e_test import test_solution
# from pipeline.d_feedback import a_feedback
import xmltojson
import json

def main():
    model = "gemma"
    context = []
    # with open('data/prompt1.txt', 'r') as file:
    #     prompt = file.read()
    #     context, response = generate_solution(prompt, context, model)
    #     print(response)
    
    # with open('data/response1.txt', 'r') as file:
    #     response = file.read()
    #     extract_and_insert(response, 'data/prompt1.java', 'data/response1.java')
    
    test_solution("_001_TwoSum")
    
    
        
        
if __name__ == "__main__":
    main()