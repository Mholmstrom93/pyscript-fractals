FROM python:latest

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# set to development mode
RUN export FLASK_ENV=development
# start the server
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]