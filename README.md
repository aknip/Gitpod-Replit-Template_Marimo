# # Gitpod - Replit - Template: Marimo

## Run in Gitpod
https://gitpod.io/#https://github.com/aknip/Gitpod-Replit-Template_Marimo

## Virtual environment using uv
- Install: curl -LsSf https://astral.sh/uv/install.sh | sh
- Create a virtual environment in current dir in folder .venv.
	- `uv venv`
- Activate environment
	- `source .venv/bin/activate`
- Deactivate environment
	- `deactivate`


uv pip install marimo==0.8.18 openai==1.42.0 langchain==0.2.14 python-docx==1.1.2 pypandoc-binary==1.13


## Install dependencies

uv pip install -r requirements.txt


# Start marimo

marimo edit 
marimo edit hello-world-marimo.py

# Run as app
marimo run hello-world-marimo.py

# Run as script from CLI
python hello-world-marimo.py

# Run / Deploy as Docker
https://docs.marimo.io/guides/deploying/deploying_docker.html

or via FastAPI App: https://docs.marimo.io/guides/deploying/programmatically.html