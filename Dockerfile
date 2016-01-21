FROM centos:7


RUN yum install -y epel-release && \
    yum install -y python-pip

ADD ./requirments.txt /app/
RUN ["pip", "install", "-r", "/app/requirments.txt"]

ADD . /app
CMD ["python", "/app/run.py"]

