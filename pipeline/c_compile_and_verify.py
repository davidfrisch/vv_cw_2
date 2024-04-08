
import subprocess
from constants import LEETCODE_MASTER_PATH, CONTAINERS_TYPE
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

def run_compile(folder_test_name: str, run_results_dir, retries_counter, verbose=False) -> int:
    cmd_2 = (f"""docker exec -w /app/leetcode-master infer ant compile.specific -Dfolder={folder_test_name}""" 
            if CONTAINERS_TYPE == "docker" 
            else  f"""singularity exec instance://infer ant -f /app/leetcode-master compile.specific -Dfolder={folder_test_name}""")
        
    print(cmd_2)
    process = subprocess.Popen(cmd_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    logs = ""
    for line in iter(process.stdout.readline, b''):
        logs += line.decode("utf-8")
        if verbose:
            print(line.decode("utf-8"), end="")
        
    # only take the javac output
    javac_errors = []
    for line in logs.split("\n"):
        javac_errors.append(line.replace("[javac] ", ""))
        if verbose and "javac" in line:
            print(line)
    
    javac_errors = "\n".join(javac_errors[1:-1])
    process.wait()
    print(f"Return compilation code: {process.returncode}")
    if process.returncode != 0:
        with open(f"{run_results_dir}/{retries_counter}_infer_logs.txt", "w") as file:
            print("Writing in "+ f"{run_results_dir}/{retries_counter}_infer_logs.txt")
            file.write(javac_errors)
        raise SyntaxError("Compilation failed")  
    
    return process.returncode


def run_infer(folder_test_name: str) -> int:
    container_name = "infer"
    cmd = (f"""docker exec -w /app/leetcode-master {container_name} infer run -- ant compile.specific -Dfolder={folder_test_name}""" 
            if CONTAINERS_TYPE == "docker"
            else f"""singularity exec instance://{container_name} sh -c "cd /app/leetcode-master && infer run -- ant compile.specific -Dfolder={folder_test_name}" """)
    
    print(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logs = ""
    for line in iter(process.stdout.readline, b''):
        logs += line.decode("utf-8")
    
    process.wait()
    return process.returncode, logs



def infer_report(run_results_dir: str, retries_counter: int):
  infer_report_path = f"{LEETCODE_MASTER_PATH}/infer-out/report.json"
  if not os.path.exists(infer_report_path):
    with open(f"{run_results_dir}/{retries_counter}_infer_report.txt", "w") as file:
      file.write("No report generated")
    
    return
  
  
  
  with open(infer_report_path, "r") as file:
    data = json.load(file)
    num_issues = len(data)
    
    for issue in data:
      print(issue['bug_type'])
    
    print(f"Number of issues: {num_issues}")
    
    report_path = f"{run_results_dir}/{retries_counter}_infer_report.json"
    with open(report_path, "w") as file:
      issues = [{"bug_type": issue['bug_type'], "qualifier": issue['qualifier']} for issue in data]
      file.write(json.dumps({
          "num_issues": num_issues,
          "issues": issues
      }))
        
      print(f"Open: {report_path}")
  

def infer_report_logs(run_results_dir: str, retries_counter: int):
  logs_file = f"{LEETCODE_MASTER_PATH}/infer-out/logs"
  with open(logs_file, "r") as file:
    logs = file.read()
    compile_errors = []
    for line in logs.split("\n"):
      if line.startswith("["):
        continue
      if "*** Infer needs a working compilation command to run." in line:
        break
      
      compile_errors.append(line)
      
  with open(f"{run_results_dir}/{retries_counter}_infer_logs.txt", "w") as file:
    for line in compile_errors:
      file.write(line)
      file.write("\n")
      



def compile_and_verify(folder_test_name: str, run_results_dir: str, retries_counter, verbose=False):
    
    compile_return_code = run_compile(folder_test_name, run_results_dir, retries_counter, verbose)
    
    print(f"Return code: {compile_return_code}")
    
    if compile_return_code != 0:
        print("Ant Compilation failed")
        raise Exception("Ant Compilation failed")
      
    infer_return_code, infer_logs = run_infer(folder_test_name)
    print(f"Infer Return code: {infer_return_code}")

    if infer_return_code != 0:
        infer_report_logs(run_results_dir, retries_counter)
        print()
        
    if infer_return_code == 0:
        with open(f"{run_results_dir}/{retries_counter}_infer_logs.txt", "w") as file:
            file.write(infer_logs)
            

  
    infer_report(run_results_dir, retries_counter)