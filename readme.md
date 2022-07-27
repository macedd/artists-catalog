
Start

    docker-compose build
    docker-compose up -d

First run

    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser