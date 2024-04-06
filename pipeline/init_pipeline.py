from constants import LEETCODE_MASTER_PATH, ALLOWED_MODELS, OLLAMA_API_URL, OPENAI_API_KEY, OLLAMA_MODELS, OPENAI_MODELS
import subprocess
import os

def validate_args(model:str, number_of_questions: int, questions_folders: list):
    if number_of_questions > len(questions_folders):
        raise ValueError(f"Number of questions to process is greater than the total number of questions. Total number of questions: {len(questions_folders)}")
    if number_of_questions < 1:
        raise ValueError(f"Number of questions to process must be greater than 0")
    if model is None:
        raise ValueError(f"Model is required")
    if model not in ALLOWED_MODELS:
        raise ValueError(f"Model not supported")
    if model in OLLAMA_MODELS and OLLAMA_API_URL is None:
        raise ValueError(f"OLLAMA_API_URL is required")
    if model in OPENAI_MODELS and OPENAI_API_KEY is None:
        raise ValueError(f"OPENAI_API_KEY is required")



def get_folders_test_names():
    leetcode_questions_src = f"{LEETCODE_MASTER_PATH}/src"
    
    # show folder names
    questions_folders = []
    for folder in os.listdir(leetcode_questions_src):
        if not folder.startswith("_"):
            continue
        if os.path.isdir(os.path.join(leetcode_questions_src, folder)):
            questions_folders.append(folder)
            
    questions_folders.sort()
    return questions_folders


def copy_original_code(original_leetcode_question, copy_leetcode_question):
    with open(original_leetcode_question, 'r') as file:
        leetcode_question = file.read()
        with open(copy_leetcode_question, 'w') as file:
            file.write(leetcode_question)
            print(f"Copy: {copy_leetcode_question}")

def clean_run_results(run_results_dir):
    for file in os.listdir(run_results_dir):
        if file.endswith(".txt") or file.endswith(".json"):
            os.remove(os.path.join(run_results_dir, file))
    print(f"Clean: {run_results_dir}")
    
def delete_bin_folder():
    bin_folder = f"{LEETCODE_MASTER_PATH}/bin"
    cmd = f"docker exec -w /app/leetcode-master infer run -- rm -rf {bin_folder}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    print(f"Delete: {bin_folder}")
