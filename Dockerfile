FROM python:3.7

COPY ./src /src
COPY ./requirements.txt /requirements.txt
COPY ./.env /.env

WORKDIR /src

RUN pip install -r requirements.txt
EXPOSE 8000

RUN uvicorn main:app --reload --host 0.0.0.0 --port 8000
