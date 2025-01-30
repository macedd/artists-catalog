## Backend Application

**First run**

    cp my-sample.cnf my.cnf
    ln -s deployments/docker-compose-local.yml deployments/docker-compose.override.yml

    cd deployments
    docker-compose exec db mysql -e "create database catalog"

**Start application**

    cd deployments
    docker-compose build
    docker-compose run web install
    docker-compose run web migrate
    docker-compose run web build
    docker-compose up -d

**Admin startup**

    docker-compose exec web pipenv run python manage.py createsuperuser
    docker-compose exec web pipenv run python manage.py createcachetable


**Development**

    # make app migrations
    docker-compose exec web \
        pipenv run python manage.py makemigrations artists

**Translations**

    # create/update languages
    django-admin makemessages -l pt_BR
    # compile languages
    django-admin compilemessages

**Debug Django**

    docker ps
    docker attach $containerID
    # quit with ctrl+p ctrl+q

## Frontend Application

**Frontends only**

    cd deployments
    docker-compose run --no-deps -p 5173:5173 web frontend

## Configuration

Select a docker compose override

    ln -s deployments/docker-compose-local.yml deployments/docker-compose.override.yml

Configure the django mysql configuration

    cp my-sample.cnf my.cnf