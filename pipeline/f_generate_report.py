import json


def generate_report(run_results_dir, folder_question_name, model, passed, total_retries,  verbose):
   
    filename = f"{run_results_dir}/final_report.json"
    
    final_report = {
        "total_retries": total_retries,
        "model": model,
        "leetcode_question": folder_question_name,
        "passed": passed,
        "tries": {}
    }
    
    all_retries = {}
    for retries_counter in range(total_retries):
        print(f"Generateeee: {retries_counter}")
        retry_report = {}
      
        """ Prompt """
        try:
            with open(f"{run_results_dir}/{retries_counter}_prompt.json") as file:
                prompt_file = json.load(file)
                retry_report["extra_prompt"] = prompt_file["extra_prompt"]
        except FileNotFoundError:
            retry_report["extra_prompt"] = None
            
        """ Response """
        try: 
            with open(f"{run_results_dir}/{retries_counter}_response.json") as file:
                file = file.read()
                response_file = json.loads(file)
                retry_report["is_extracted"] = response_file["is_extracted"]
                retry_report["number_of_code_blocks"] = response_file["number_of_code_blocks"]
                retry_report["extra_information_num_words"] = response_file["extra_information_num_words"]
                retry_report["response"] = response_file["response"]
        except FileNotFoundError:
            retry_report["is_extracted"] = None
            retry_report["number_of_code_blocks"] = None
            retry_report["extra_information_num_words"] = None
            retry_report["response"] = None
            
        """ Compile and Verify """
        try:  
            with open(f"{run_results_dir}/{retries_counter}_infer_report.json") as file:
                infer_report = json.load(file)
                retry_report["number_of_issues"] = len(infer_report["issues"])
                retry_report["issues"] = infer_report["issues"]
                
        except FileNotFoundError:
            retry_report["number_of_issues"] = None
            retry_report["issues"] = None
        
        """ Test Solution """
        try:
            with open(f"{run_results_dir}/{retries_counter}_tests_results.json") as file:
                tests_results = json.load(file)
                retry_report["num_tests"] = tests_results["num_tests"]
                retry_report["num_successes"] = tests_results["num_successes"]
                retry_report["num_failures"] = tests_results["num_failures"]
                retry_report["num_errors"] = tests_results["num_errors"]
                retry_report["timestamp"] = tests_results["timestamp"]
                retry_report["test_cases"] = tests_results["test_cases"]
                
        except FileNotFoundError:
            retry_report["num_tests"] = None
            retry_report["num_successes"] = None
            retry_report["num_failures"] = None
            retry_report["num_errors"] = None
            retry_report["timestamp"] = None
            retry_report["test_cases"] = None
            
        all_retries[retries_counter] = retry_report


    final_report["tries"] = all_retries
    
    with open(filename, 'w') as file:
        file.write(json.dumps(final_report, indent=4))
        print(f"Open: {filename}")
    
    