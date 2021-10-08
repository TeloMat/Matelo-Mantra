# base image
FROM python:3.9.5
# setup environment variable


#ENV PYTHONBUFFERED=1
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./.env.staging ./.env
#CMD ["gunicorn", "--bind", ":8000", "--workers","3", "core.wsgi:application"]

ENTRYPOINT ["sh", "start.sh"]
