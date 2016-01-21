FROM python:3-alpine


ADD ./requirments.txt /app/
RUN ["pip", "install", "-r", "/app/requirments.txt"]

ENV REDIS_MASTER_PORT_6379_TCP_ADDR='localhost' \
    REDIS_MASTER_PORT_6379_TCP_PORT=6379

ADD . /app
CMD ["python3", "/app/run.py"]

