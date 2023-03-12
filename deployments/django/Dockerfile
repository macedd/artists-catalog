# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

RUN apt-get update && \
  apt-get install -y \
            gettext \
            npm

RUN npm -g install less
RUN python -m pip install \
                  pipenv

ENV NVM_DIR /usr/local/nvm
RUN mkdir $NVM_DIR && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
RUN . $NVM_DIR/nvm.sh \
    && nvm install 16 \
    && nvm alias default 16 \
    && nvm use default

ENTRYPOINT /code/deployments/django/entrypoint.sh
RUN ln -s /code/deployments/django/entrypoint.sh /usr/local/bin/entrypoint.sh

ENV UID=1000
RUN useradd -r -u $UID -g root django
USER django
