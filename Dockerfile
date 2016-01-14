FROM python:3-alpine

ADD . /app

RUN ["pip", "install", "-r", "/app/requirments.txt"]

CMD ["python3", "/app/run.py"]

