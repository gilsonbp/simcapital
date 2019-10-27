#!/bin/bash

# wait for Postgres to start
sleep 10

# Django
pip install -r /src/requirements.txt
python /src/manage.py migrate

# Gunicorn
gunicorn simcapital.wsgi:application \
  --bind 0.0.0.0:8000 \
  --log-file=/src/logs/gunicorn_error.log \
  --access-logfile=/src/logs/gunicorn_access.log
