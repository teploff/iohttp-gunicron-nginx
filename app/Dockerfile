FROM python:3.7-alpine

MAINTAINER Alexander Teplov <teplov_aa@rtsoft.ru>
LABEL maintainer="teplov_aa@rtsoft.ru"

WORKDIR /app

COPY . .

RUN apk add gcc libc-dev && pip install -r requirements.txt

CMD [ "gunicorn", "main:web_app", "--bind", "0.0.0.0:8080", "--worker-class", "aiohttp.GunicornWebWorker"]