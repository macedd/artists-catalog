
Start

    cd deployments
    docker-compose build
    docker-compose run web install
    docker-compose run web migrate
    docker-compose run web build
    docker-compose up -d

First run

    ln -s `pwd`/deployments/docker-compose-local.yml deployments/docker-compose.override.yml
    docker-compose exec db mysql -e "create database catalog"
    docker-compose exec web pipenv run python manage.py createsuperuser

App bootstrap

    docker-compose exec web entrypoint.sh install
    docker-compose exec web entrypoint.sh migrate
    docker-compose exec web entrypoint.sh build

Development

    # make app migrations
    docker-compose exec web \
        pipenv run python manage.py makemigrations artists

Translations

    # create/update languages
    django-admin makemessages -l pt_BR
    # compile languages
    django-admin compilemessages

Frontends

    cd frontends
    npm install
    npm run dev

Debug Django

    docker ps
    docker attach $containerID
    # quit with ctrl+p ctrl+q