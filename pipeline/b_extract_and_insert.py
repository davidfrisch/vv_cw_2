import math
import json


def write_report(run_results_dir, counter, response, is_extracted, number_of_code_blocks, extra_information_num_words):
    filepath = run_results_dir + f"/{str(counter)}_response.json"
    
    with open(filepath, 'w') as file:
        file.write(json.dumps({
            "is_extracted": is_extracted,
            "number_of_code_blocks": number_of_code_blocks,
            "extra_information_num_words": extra_information_num_words,
            "response": response
        }))


def extract_and_insert(response, leetcode_question_path, run_results_dir, counter):
    number_of_java_code_blocks = math.floor(response.count("```")/2)
    is_even = response.count("```") % 2 == 0
        
    if not is_even:
        write_report(run_results_dir, counter, response, is_extracted=False, number_of_code_blocks=number_of_java_code_blocks, extra_information_num_words=None)
        raise Exception("The number of Java code blocks found is not even. You may have a missing or extra code block. Only one Java code block is expected.")
    
    if number_of_java_code_blocks == 0:
        write_report(run_results_dir, counter, response, is_extracted=False, number_of_code_blocks=number_of_java_code_blocks, extra_information_num_words=None)
        raise Exception("No Java code block found in the given response.")
      
    if number_of_java_code_blocks > 1:
        write_report(run_results_dir, counter, response, is_extracted=False, number_of_code_blocks=number_of_java_code_blocks, extra_information_num_words=None)
        raise Exception("More than one Java code block found in the response, Only one Java code block is expected.")
    
    response = response.replace("```java", "```")
    begin = response.find("```")
    end = response.find("```", begin+3)
    code = response[begin+3:end]
    
    with open(leetcode_question_path, 'w') as file:
        file.write(code)
    
    with open(run_results_dir + f"/{str(counter)}_response_extracted_code.txt", 'w') as file:
        file.write(code)
    
    extra_information_num_words = len(response.replace(code, "").strip().split(" "))
    write_report(run_results_dir, counter, response, True, number_of_java_code_blocks, extra_information_num_words)    