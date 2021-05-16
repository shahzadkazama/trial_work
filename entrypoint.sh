#!/bin/bash

cd /code/Swyft

echo "Making migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting gunicorn"

gunicorn --workers 3 --bind 0.0.0.0:8000 Swyft.wsgi &
rm /etc/nginx/sites-enabled/default

echo "Starting nginx"
/usr/sbin/nginx

gunicorn --timeout 1800 --access-logfile - --workers 3 --bind unix:/code/Swyft/Swyft.sock Swyft.wsgi:application

sleep 10000
