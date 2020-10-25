FROM python:3-slim
WORKDIR /app
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential libpq-dev
RUN pip install --no-cache-dir flask flask-sqlalchemy psycopg2