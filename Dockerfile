FROM python:3-alpine


ADD ./requirments.txt /app/
RUN ["pip", "install", "-r", "/app/requirments.txt"]

ADD . /app
CMD ["python3", "/app/run.py"]

