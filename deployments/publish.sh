#!/usr/bin/bash

HOST=${1}
FOLDER=${2}
COMMAND=${3:-publish}
BASEDIR=`realpath $(dirname "$0")/../`

echo "HOST=$HOST COMMAND=$COMMAND"

if [[ $COMMAND = "publish" ]]
then

    TMP_FOLDER="$FOLDER/tmp"
    APP_FOLDER="$FOLDER/catalog"

    cd $BASEDIR
    git archive -o ../catalog.zip HEAD
    scp ../catalog.zip "$HOST":~
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

else

    echo "$COMMAND command not implemented"

fi
