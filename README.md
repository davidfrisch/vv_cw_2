# Coursework 3 - Validation and Verification
In this project, we're investigating how well language models (LLMs) of different sizes can solve LeetCode problems in Java code. In particular, we're interested in whether smaller, more manageable LLMs can compete with larger ones, while still running smoothly on a regular computer. 
This Github repository provides the necessary code to run such a system that can handle all three parts of the problem: setting up the prompt for the LLM, getting the code snippet response, and checking that the response actually works.


## Setup
The setup guide is available in the [setup guide](./setup.md). 
It provides a step-by-step guide to setting up the project. 


## Run 
```bash
source venv/bin/activate
cd pipeline
python3 main.py --model <model_name> --number <number_of_problems_to_solve> --verbose <True/False>
```


