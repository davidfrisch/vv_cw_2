import xmltojson
import json
from tree_sitter_languages import get_parser
from constants import LEETCODE_MASTER_PATH
import subprocess
import os

parser = get_parser('java')

dir_path = os.path.dirname(os.path.realpath(__file__))
def run_junit_test(folder_test_name: str):
    leetcode_master_path = dir_path + "/../leetcode-master"
    cmd = f"cd {leetcode_master_path} && ant test.specific -Dtest.folder={folder_test_name}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    for line in process.stdout:
        print(line)
        
    process.communicate()


def find_methode_code(method_name, methods_code):
    for method in methods_code:
        name = method[0]
        code = method[1]
        if method_name in name:
            return code
          
    return None


def extract_methods_with_implementation(node, code):
    methods = []
    if node.type == "method_declaration":
        method_name_node = node.children[2]
        method_name = code[method_name_node.start_byte: method_name_node.end_byte]
        if not method_name.strip().startswith("Test"):
            return []
        method_body = code[node.start_byte: node.end_byte]
        methods.append((method_name.strip(), method_body.strip()))
    for child in node.children:
        methods.extend(extract_methods_with_implementation(child, code))
    
    return methods

def test_solution(folder_test_name: str):
  run_junit_test(folder_test_name)
  with open(f"{LEETCODE_MASTER_PATH}/test/{folder_test_name}/PracticeTest.java", 'r') as file:
    code = file.read()
  
  tree = parser.parse(bytes(code, 'utf8'))
  methods_code = extract_methods_with_implementation(tree.root_node, code)
  
  
  with open(f"{LEETCODE_MASTER_PATH}/report/TEST-{folder_test_name}.PracticeTest.xml") as file:
        my_xml = file.read()
        json_file = xmltojson.parse(my_xml)
        
  json_file = json.loads(json_file)
  num_tests = json_file['testsuite']['@tests']
  num_failures = json_file['testsuite']['@failures']
  num_errors = json_file['testsuite']['@errors']
  timestamp = json_file['testsuite']['@timestamp']
  test_cases = []
  for test in json_file['testsuite']['testcase']:
      # find the methode implementation in methods_code
      methode_code = find_methode_code(test['@name'], methods_code)
      test_cases.append({
          'name': test['@name'],
          'time': test['@time'],
          'success': 'failure' not in test,
          'failure': test['failure'] if 'failure' in test else None,
          'message': test['failure']['@message'] if 'failure' in test else '',
          'code': methode_code
      })
  
 
  
  for test in test_cases:
      if not test['success']:
          print(test['name'])
          print(test['message'])
          print(test['code'])
          print('------------------------------------')
        
  print(f"Number of tests: {num_tests}")
  print(f"Number of successes: {int(num_tests) - int(num_failures) - int(num_errors)}")
  print(f"Number of failures: {num_failures}")
  print(f"Number of errors: {num_errors}")
  print(f"Timestamp: {timestamp}")