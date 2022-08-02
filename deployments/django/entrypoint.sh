#!/usr/bin/env bash

COMMAND=${1:-dev}

if [[ $COMMAND = "dev" ]]; then

    cd apps/theme/static_src
    npx tailwindcss -i ./tailwind.css -o ../static/theme/tailwind.css --watch &

    cd -
    python manage.py runserver 0.0.0.0:8000

elif [[ $COMMAND = "build" ]]; then

    cd apps/theme/static_src
    npx tailwindcss -i ./tailwind.css -o ../static/theme/tailwind.css --minify

elif [[ $COMMAND = "prod" ]]; then

    gunicorn config.wsgi

else
    echo "$COMMAND command not implemented"
    exec "$@"
fi
