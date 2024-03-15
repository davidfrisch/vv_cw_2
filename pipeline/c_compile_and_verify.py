
import subprocess
from constants import LEETCODE_MASTER_PATH
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

def run_infer(folder_test_name: str):
    container_name = "infer"
    cmd = f"""  docker exec -w /app/pipeline/data {container_name} infer run -- javac /app/leetcode-master/src/{folder_test_name}/Practice.java"""
    print(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # for line in process.stdout:
    #     print(line)
        
    process.wait()
    return process.returncode


def infer_report():
  report = f"data/infer-out/report.json"
  with open(report, "r") as file:
    data = json.load(file)
    
  num_issues = len(data)
  for issue in data:
    qualifier = issue['qualifier']
    bug_type = issue['bug_type']
    print(issue['bug_type'])
    print(f"Qualifier: {qualifier}")
  print(f"Number of issues: {num_issues}")

    

def compile_and_verify(folder_test_name: str):
    infer_return_code = run_infer(folder_test_name)
    print(f"Return code: {infer_return_code}")
    if infer_return_code != 0:
        print("Compilation failed")
        raise Exception("Compilation failed")
  
    infer_report()