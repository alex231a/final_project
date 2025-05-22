#!/bin/bash

source /home/oyakovenko/venv/bin/activate

cd /home/oyakovenko/django-oscar || exit 1

{
  echo "=== DEPLOY STARTED: $(date) ==="

  echo "--- Git pull ---"
  git pull origin master

  echo "--- Installing requirements ---"
  pip install -r requirements.txt

  echo "--- Applying migrations ---"
  python manage.py makemigrations --noinput
  python manage.py migrate --noinput

  echo "--- Collecting static files ---"
  python manage.py collectstatic --noinput

  echo "=== DEPLOY COMPLETED: $(date) ==="
} >> /home/oyakovenko/django-oscar/deploy_log.log 2>&1

