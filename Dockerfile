FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /project
COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .