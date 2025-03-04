FROM python:3.9

RUN apt-get update && apt-get install -y openssh-client

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD python3 manage.py runserver 0.0.0.0:8000
