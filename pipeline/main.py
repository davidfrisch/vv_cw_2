from constants import LEETCODE_MASTER_PATH, ALLOWED_MODELS
from init_pipeline import validate_args, get_folders_test_names, copy_original_code, clean_run_results, delete_bin_folder
from a_generate_solution import generate_solution
from b_extract_and_insert import extract_and_insert
from c_compile_and_verify import compile_and_verify
from d_test import test_solution
import os
from datetime import datetime
import argparse

dir_path = os.path.dirname(os.path.realpath(__file__))
MAX_NUMBER_RETRIES = 2


def main(model, number_of_questions=5, benchmark=False, verbose=False):
    questions_folders = get_folders_test_names()
    validate_args(model, number_of_questions, benchmark, questions_folders)
    delete_bin_folder()
    
    
    for folder_question_name in questions_folders[:number_of_questions]:
        context = []
        retries_counter = 0
        error_message = ""
        print(f"Processing: {folder_question_name}")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S") if benchmark else ""
        original_leetcode_question = f"{LEETCODE_MASTER_PATH}/src/{folder_question_name}/original.txt"
        leetcode_question_path = f"{LEETCODE_MASTER_PATH}/src/{folder_question_name}/Practice.java"
        run_results_dir = f"{dir_path}/data/{timestamp}_{folder_question_name}"
        os.makedirs(run_results_dir, exist_ok=True)
        clean_run_results(run_results_dir)
        
        while retries_counter < MAX_NUMBER_RETRIES:
            prompt_path = f"{run_results_dir}/{retries_counter}_prompt.txt"
            response_path = f"{run_results_dir}/{retries_counter}_response.txt"
            try:
                if retries_counter == 0:
                    copy_original_code(original_leetcode_question, leetcode_question_path)
                
                """*** Generate Solution with LLM Algorithm ***"""
                with open(leetcode_question_path, 'r') as file:
                    leetcode_question = file.read()
                    
                    prompt = (f"Replace  // TODO Auto-generated method stub with your solution code. Only answer with the complete file. Don't explain \n {leetcode_question}" 
                                  if retries_counter == 0 
                                  else f"Your code has the following error: {error_message}\n Retry with a fix and give the complete file. Don't explain. Only give java code \n {leetcode_question}")

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
                compile_and_verify(folder_question_name, run_results_dir, retries_counter)
                error_message = ""
            
            
                # """*** Test Solution ***"""
                test_solution(folder_question_name, run_results_dir, retries_counter)
                retries_counter = MAX_NUMBER_RETRIES
                print(f"Done: {folder_question_name}")
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
            
        copy_original_code(original_leetcode_question, leetcode_question_path)
        
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
  parser.add_argument("-b", "--benchmark", action="store_true", help="Enable benchmark mode")
  parser.add_argument("-m", "--model", type=str, help="Model to use")
  parser.add_argument("-n", "--number", type=int, help="Number of questions to process")
  args = parser.parse_args()

  verbose = args.verbose
  benchmark = args.benchmark
  model = args.model
  number = args.number
  
  # model = "gemma"
  # model = "llama2:latest"
  model = "gpt-3.5-turbo-0125"
  main(model, number, benchmark, verbose)