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

#ADD ./mounts ./
#
#ADD ./media ./
#
#VOLUME ./db.sqlite3

COPY ./.env.heroku ./.env
CMD ["gunicorn", "--bind", ":8000", "--workers","3", "core.wsgi:application"]

