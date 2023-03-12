#!/usr/bin/env bash

COMMAND=${1:-dev}

export PIPENV_VENV_IN_PROJECT=1

echo "COMMAND=$COMMAND"

source /usr/local/nvm/nvm.sh
nvm use 16

if [[ $COMMAND = "dev" ]]; then

    cd apps/theme/static_src
    npx tailwindcss -i ./tailwind.css -o ../static/theme/tailwind.css --watch &

    cd -
    pipenv run \
        python manage.py runserver 0.0.0.0:8002

elif [[ $COMMAND = "build" ]]; then

    # build frontend
    cd frontends
    npm run build-only
    # django collect
    cd -
    pipenv run \
        python manage.py collectstatic --noinput

elif [[ $COMMAND = "prod" ]]; then

    export GUNICORN_CMD_ARGS="--name=artists-catalog --bind=0.0.0.0:8000 --workers=3 --worker-class=gevent"
    pipenv run \
        gunicorn --capture-output config.wsgi

elif [[ $COMMAND = "reload" ]]; then

    kill -HUP `pgrep --ns 1 "^(gunicorn|python)"`

elif [[ $COMMAND = "migrate" ]]; then

    pipenv run \
        python manage.py migrate --noinput

elif [[ $COMMAND = "install" ]]; then

    # python backend
    pipenv install
    # javasript frontend
    cd frontends
    npm install

elif [[ $COMMAND = "frontend" ]]; then

    cd frontends
    npm install
    npm run dev

else
    echo "$COMMAND command not implemented"
    exec "$@"
fi
