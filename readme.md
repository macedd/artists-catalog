
Start

    docker-compose build
    docker-compose up -d

First run

    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser

Development

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt