# base image
FROM python:3.9.5
# setup environment variable

ENV PYTHONBUFFERED=1
WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .
RUN chmod +x ./start.sh
CMD ./start.sh

