# Using Distroless image of python
FROM python:3.9-slim-bullseye
WORKDIR /app/
COPY . /app/
COPY requirements.txt /app/
RUN apt-get update &&  apt-get install -y python3 python3-pip python3-venv
SHELL ["/bin/bash","-c"]
RUN python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt 
EXPOSE 5000
CMD source venv/bin/activate && python3 app.py 
