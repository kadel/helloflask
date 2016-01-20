FROM python:3-alpine


ADD ./requirments.txt /app/
RUN ["pip", "install", "-r", "/app/requirments.txt"]

ENV REDIS_HOST='localhost' \
    REDIS_PORT=6379



ADD . /app
CMD ["python3", "/app/run.py"]

