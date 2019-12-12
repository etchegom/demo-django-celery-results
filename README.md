# Demo how to use [django-celery-results](https://github.com/celery/django-celery-results) to store Celery task results using the Django ORM and the Postgres specific [JSONField](https://docs.djangoproject.com/fr/3.0/ref/contrib/postgres/fields/#django.contrib.postgres.fields.JSONField)


## Requirements
- Docker
- Docker-compose

## Expected behavior
...


## Run the demo

- Run the docker stack
```
docker-compose up -d --build
```

- Create a superuser account and login django admin
```
docker-compose run --rm app python manage.py createsuperuser
```

- Create users in django admin, then trigger the demo celery task and check results in django admin
```
docker-compose run --rm app python manage.py trigger_task
```

