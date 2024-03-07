FROM python:3.11.7-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./projeto /app

COPY ./entrypoint.sh /app

ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]