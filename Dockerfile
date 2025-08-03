# Using Distroless image of python
FROM python:3.9-slim-bullseye
WORKDIR /app/
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["python","app.py"]
