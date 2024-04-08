from constants import LEETCODE_MASTER_PATH, OLLAMA_MODELS
import json
from init_pipeline import validate_args, get_folders_test_names, copy_original_code, clean_run_results, delete_bin_folder
from a_generate_solution import generate_solution
from b_extract_and_insert import extract_and_insert
from c_compile_and_verify import compile_and_verify
from d_test import test_solution
from f_generate_report import generate_report
import os
import argparse

dir_path = os.path.dirname(os.path.realpath(__file__))



def main(model, number_of_questions=5, max_retries = 5, verbose=False):
    questions_folders = get_folders_test_names()
    print(f"Using model: {model}")
    validate_args(model, number_of_questions, questions_folders)
    delete_bin_folder()
    
    
    for folder_question_name in questions_folders[:number_of_questions]:
        context = []
        passed = False
        succeded_counter = max_retries
        retries_counter = 0
        error_message = ""
        print(f"Processing: {folder_question_name}")
        original_leetcode_question = f"{LEETCODE_MASTER_PATH}/src/{folder_question_name}/original.txt"
        leetcode_question_path = f"{LEETCODE_MASTER_PATH}/src/{folder_question_name}/Practice.java"
        folder_model = model.replace(":", "_")
        run_results_dir = f"{dir_path}/data/{folder_model}/{folder_question_name}"
        os.makedirs(run_results_dir, exist_ok=True)
        clean_run_results(run_results_dir)
        
        while retries_counter < max_retries:
            prompt_path = f"{run_results_dir}/{retries_counter}_prompt.txt"
            prompt_json_path = f"{run_results_dir}/{retries_counter}_prompt.json"
            response_path = f"{run_results_dir}/{retries_counter}_response.txt"
            try:
                if retries_counter == 0:
                    copy_original_code(original_leetcode_question, leetcode_question_path)
                
                """*** Prompt Consutrction ***"""
                with open(leetcode_question_path, 'r') as file:
                    leetcode_question = file.read()
                    
                    extra_prompt = (f"Replace  // TODO Auto-generated method stub with your solution code. Only answer with the complete file. Don't explain !"
                                  if retries_counter == 0
                                  else f"The following code has the following error: {error_message}\n. Retry with a fix of the complete file. Don't explain! Only give the java code")
                    
                    with open(prompt_json_path, 'w') as file:
                        file.write(json.dumps({"extra_prompt": extra_prompt}))
                    
                    prompt = f"{extra_prompt}\n{leetcode_question}"
                    
                    
                    """*** Generate Solution with LLM Algorithm ***"""
                    with open(prompt_path, 'w') as file:
                        file.write(prompt)
                        print("Open: ", prompt_path)
                        context = []
                        context, response = generate_solution(prompt, context, model)
                        with open(response_path, 'w') as file:
                            file.write(response)
                            print("Open: ", response_path)
                    

                """*** Extract and Insert ***"""
                with open(response_path, 'r') as file:
                    llm_algo_response = file.read()
                    extract_and_insert(llm_algo_response, leetcode_question_path, run_results_dir, retries_counter)
            
            
                # """*** Compile and Verify ***"""
                compile_and_verify(folder_question_name, run_results_dir, retries_counter, verbose)
                error_message = ""
            
            
                # """*** Test Solution ***"""
                test_solution(folder_question_name, run_results_dir, retries_counter, verbose)
                
                
               
                print(f"Done: {folder_question_name}")
                passed = True
                succeded_counter = retries_counter + 1
                retries_counter = max_retries
                break
            
          
            
            except SyntaxError as e:
                print(f"Syntax Error: {e}")
                with open(run_results_dir + f"/{retries_counter}_infer_logs.txt", "r") as file:
                    error_message = file.read()
                    retries_counter += 1
                    print(f"Retrying: {retries_counter}")
                    print(f"Error: {error_message}")
            except ValueError as e:
                print(f"Value Error: {e}")
                with open(run_results_dir + f"/{retries_counter}_tests_logs.txt", "r") as file:
                    error_message = file.read()
                    retries_counter += 1
                    print(f"Retrying: {retries_counter}")
                    verbose and print(f"Error: {error_message}")       
            except KeyboardInterrupt:
                os._exit(1)
            except Exception as e:
                print(f"Error: {e}")
                error_message = str(e)
                retries_counter += 1
                print(f"Retrying: {retries_counter}")
                print(f"Error: {error_message}")
            
        
        """*** Generate Report ***"""
        generate_report(run_results_dir, folder_question_name, model, passed, succeded_counter, verbose)
                
        copy_original_code(original_leetcode_question, leetcode_question_path)
        
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-m", "--model", type=str, help="Model to use")
  parser.add_argument("-n", "--number", type=int, help="Number of questions to process", default=5)
  parser.add_argument("-r", "--retries", type=int, help="Number of retries", default=5)
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
  args = parser.parse_args()

  model = args.model
  number = args.number
  max_retries = args.retries
  verbose = args.verbose
  
  # model = "deepseek-coder:6.7b-instruct"
  # model = "gemma"
  # model = "llama2:latest"
  # model = "mistral:instruct"
  model = "gpt-3.5-turbo-0125"
  number = 1
  max_retries = 3
  main(model, number, max_retries, verbose)