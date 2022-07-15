# pyscript-fractals
A pyscript app with interactive fractals

# Installation
You can run the app locally, either with flask internal server or via docker. 

## Run with flask
With this option nothing needs to be installed.
just run the following commands.

(if you want development mode)
export FLASK_ENV=development

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
run flask

## Run with docker
For this to work docker needs to be installed. And syntax is for later docker versions that come with docker compose installed. 

docker build -t pyscript-fractals .
docker compose up
