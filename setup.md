# Requirements

## VSCode 
To run the application you need to have Visual Studio Code installed on your machine. You can download it from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/). Please make sure to have the latest version installed, the pipeline has been tested with version 1.88.0 (Universal).

## Install Docker
To run the application you need to have Docker installed on your machine. You can download it from the official website: [https://www.docker.com/get-started](https://www.docker.com/get-started)

## Python3.9
To run the application you need to have Python3.9 installed on your machine. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/) or via package manager.

# Installation

## Install the required python packages
To install the required packages, run the following command in the root directory of the project:

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Start the docker containers
To start the docker containers, run the following command in the root directory of the project:

```bash
docker compose pull
docker compose up -d
```

if you only want to start the infer container run the following command:

```bash
docker compose pull infer
docker compose up -d infer
```

### Pull the Ollama models
To pull the Ollama models, run the following command in the root directory of the project:

```bash
docker exec -it ollama ollama pull mistral:instruct
docker exec -it ollama ollama pull deepseek-coder:6.7b-instruct
docker exec -it ollama ollama pull gemma:7b-instruct
docker exec -it ollama ollama pull llama2:13b
docker exec -it ollama ollama pull codellama:13b-code
```

## Start Ollama from a remote server

### From another machine with docker installed
To start the Ollama server from another machine with docker installed, run the following command:

```bash
git clone https://github.com/davidfrisch/vv_cw_2.git
cd vv_cw_2
docker compose up -d ollama
```

Then you need to make the port 11434 accessible for external connections with port forwarding. You can do this by following the instructions on the official website: [https://code.visualstudio.com/docs/editor/port-forwarding](https://code.visualstudio.com/docs/editor/port-forwarding). 
Make sure to forward the port 11434 and change the visiblity to `public`. To change the visibility to `public` you need to be on the PORTS tab, then right click on the current "visibility" column > ports visibility > public. The link should look like this: `https://random_strings-11434.uks1.devtunnels.ms`.

Finally pull the Ollama models by running the following command:

```bash
docker exec -it ollama ollama pull mistral:instruct
docker exec -it ollama ollama pull deepseek-coder:6.7b-instruct
docker exec -it ollama ollama pull gemma:7b-instruct
docker exec -it ollama ollama pull llama2:13b
docker exec -it ollama ollama pull codellama:13b-code
```

### From a Linux computer from the UCL Lab with singularity installed
If your home directory has limited space in the UCL computers, you should ask a system administrator to create you a path with enough space to download the models. Then you can create a symbolic link to the Ollama default directory. You can do this by running the following command:

```bash
ln -s /your/path/with/enough/space  ~/.ollama
````

Then you can start the Ollama container by running the following command:

```bash
singularity instance start --nv docker://ollama/ollama ollama
```
The --nv flag is optional and is used to enable GPU acceleration. 

Then you need to start the ollama server by running the following command:

```bash
singularity exec instance://ollama ollama serve
```

With a new terminal, you can pull the Ollama models by running the following command:
```bash
singularity exec instance://ollama ollama pull mistral:instruct
singularity exec instance://ollama ollama pull deepseek-coder:6.7b-instruct
singularity exec instance://ollama ollama pull gemma:7b-instruct
singularity exec instance://ollama ollama pull llama2:13b
singularity exec instance://ollama ollama pull codellama:13b-code
```

Finally open the port 11434 for external connections with port forwarding. You can do this by following the instructions on the official website: [https://code.visualstudio.com/docs/editor/port-forwarding](https://code.visualstudio.com/docs/editor/port-forwarding). 
Make sure to forward the port 11434 and change the visiblity to `public`. To change the visibility to `public` you need to be on the PORTS tab, then right click on the current "visibility" column > ports visibility > public. The link should look like this: `https://random_strings-11434.uks1.devtunnels.ms`.

Test the connection by running the following command:

```bash
curl https://random_strings-11434.uks1.devtunnels.ms
```

To stop the Ollama container, run the following command:

```bash
singularity instance stop ollama
```


## Create the .env file
To create the .env file, run the following command in the root directory of the project:

```bash
touch pipeline/.env
```
Then add the following content to the .env file:

```bash
OLLAMA_API_URL=https://random_strings-11434.uks1.devtunnels.ms
OPENAI_API_KEY=sk-1234567890
```

Make sure to replace the `OLLAMA_API_URL` with the URL you got from the port forwarding and the `OPENAI_API` with your OpenAI API key.

You should now be able to run the application by running the following command in the root directory of the project:

```bash
source venv/bin/activate
cd pipeline
python3 main.py --model mistral:instruct --number 3 --verbose True
```