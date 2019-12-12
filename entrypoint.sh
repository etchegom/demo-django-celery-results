#!/bin/bash

set -e

case $1 in
    server)
        exec python manage.py migrate && python manage.py runserver 0.0.0.0:8000
        ;;
    worker)
        exec celery worker --app=example --loglevel=INFO
        ;;
    *)
        echo "Running server command: $@"
        exec "$@"
esac
