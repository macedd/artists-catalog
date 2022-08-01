# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

RUN apt-get update && \
  apt-get install -y gettext npm

RUN npm -g install less
RUN python -m pip install gunicorn

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ENTRYPOINT /code/deployments/django/entrypoint.sh