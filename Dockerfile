FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir \code
WORKDIR \code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN apt-get update && apt-get upgrade -y
#RUN apt-get install -y cron
#RUN python code/manage.py crontab add
