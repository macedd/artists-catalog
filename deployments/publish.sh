#!/usr/bin/bash

HOST=${1}
FOLDER=${2}
COMMAND=${3:-publish}

echo "HOST=$HOST COMMAND=$COMMAND"

if [[ $COMMAND = "publish" ]]; then

    git archive -o ../catalog.zip HEAD
    scp ../catalog.zip "$HOST":~
    ssh "$HOST" "
        unzip -q -u -o catalog.zip -d $FOLDER && \
        cd $FOLDER && \
        docker-compose build && \
        docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d && \
        docker-compose exec -T web python manage.py migrate --noinput && \
        docker-compose exec -T web python manage.py collectstatic --noinput && \
        "

else
    echo "$COMMAND command not implemented"
fi
