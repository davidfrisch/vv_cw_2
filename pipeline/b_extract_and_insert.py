import math
from tree_sitter_languages import get_parser

parser = get_parser('java')

def extract_class(tree):
    for child in tree.children:
        if child.type == 'class_declaration':
            return child          

def print_code(node, code):
    print(code[node.start_byte:node.end_byte])
    

def extract_and_insert(response, leetcode_question_path, run_results_dir, counter):
    number_of_java_code_blocks = math.floor(response.count("```")/2)
    is_even = response.count("```") % 2 == 0
    if not is_even:
        raise Exception("The number of Java code blocks found is not even. You may have a missing or extra code block. Only one Java code block is expected.")
    
    if number_of_java_code_blocks == 0:
        raise Exception("No Java code block found in the given response.")
      
    if number_of_java_code_blocks > 1:
        raise Exception("More than one Java code block found in the response, Only one Java code block is expected.")
    
    response = response.replace("```java", "```")
    begin = response.find("```")
    end = response.find("```", begin+3)
    code = response[begin+3:end]
    
    with open(leetcode_question_path, 'w') as file:
        file.write(code)
    
    with open(run_results_dir + f"/{str(counter)}_response_extracted_code.txt", 'w') as file:
        file.write(code)
    
    # tree = parser.parse(bytes(code, 'utf8'))
    # class_node = extract_class(tree.root_node)
    
    # class_code = code[class_node.start_byte:class_node.end_byte]
    # # print(class_code)
    
    # with open(original_code_file_path, 'r') as file:
    #     original_code = file.read()
    #     original_class_tree = parser.parse(bytes(original_code, 'utf8'))
    #     original_class_node = extract_class(original_class_tree.root_node)
    #     print_code(original_class_node, original_code)
        
    #     # replace the original class with the new class
    #     new_code = original_code[:original_class_node.start_byte] + class_code + original_code[original_class_node.end_byte:]
    #     print(new_code)
        
    #     with open(output_code_file_path, 'w') as file:
    #         file.write(new_code)