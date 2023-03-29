#!/usr/bin/env bash

HOST=${1}
FOLDER=${2}
COMMAND=${3:-publish}
BASEDIR=`realpath $(dirname "$0")/../`

echo "HOST=$HOST COMMAND=$COMMAND"

TMP_FOLDER="$FOLDER/tmp"
APP_FOLDER="$FOLDER/catalog"

if [[ $COMMAND = "publish" ]]
then

    cd $BASEDIR
    git archive -o $BASEDIR/../catalog.zip HEAD
    scp $BASEDIR/../catalog.zip "$HOST":~
    ssh "$HOST" "
        unzip -q -u -o ~/catalog.zip -d $APP_FOLDER && \
        cd $APP_FOLDER/deployments/ && \
        export TMPDIR=$TMP_FOLDER TMP=$TMP_FOLDER TEMP=$TMP_FOLDER; \
        mkdir -p \$TMP && \
        docker-compose build && \
        docker-compose run -T web install && \
        docker-compose up -d && \
        docker system prune -f && \
        docker-compose exec -T web entrypoint.sh migrate && \
        docker-compose exec -T web entrypoint.sh build && \
        docker-compose exec -T web entrypoint.sh reload && \
        docker-compose logs | tail -n 14"

elif [[ $COMMAND = "logs" ]]
then

    ssh "$HOST" "
        cd $APP_FOLDER/deployments/ && \
        docker-compose logs | tail -n 14"

elif [[ $COMMAND = "exec" ]]
then

    REMOTE_COMMAND="${@:4}"
    ssh "$HOST" "
        cd $APP_FOLDER/deployments/ && \
        docker-compose exec web $REMOTE_COMMAND"

else

    echo "$COMMAND command not implemented"

fi
