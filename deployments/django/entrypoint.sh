#!/usr/bin/bash

COMMAND=${1:-dev}

if [[ $COMMAND = "dev" ]]; then

    cd apps/theme/static_src
    npx tailwindcss -i ./input.css -o ../static/output.css --watch &

    cd -
    python manage.py runserver 0.0.0.0:8000

if [[ $COMMAND = "prod" ]]; then

    cd apps/theme/static_src
    npx tailwindcss -i ./input.css -o ../static/output.css

    cd -
    gunicorn config.wsgi

else
    echo "$COMMAND command not implemented"
    exec "$@"
fi
