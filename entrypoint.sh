#!/bin/bash

cd /code/Swyft
mkdir /lfls_data
mkdir /lfls_data/uploads
mkdir /lfls_data/exporter
mkdir /lfls_data/log_files
chmod 777 -R /lfls_data

#mkdir /code/dataprep_api/logs

#echo "Starting Celery"
#celery -A dataprep_api worker --loglevel=debug --logfile=celery.logs &

echo "Making migrations"
###python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting gunicorn"

gunicorn --workers 3 --bind 0.0.0.0:8000 Swyft.wsgi &
rm /etc/nginx/sites-enabled/default

echo "Starting nginx"
/usr/sbin/nginx

echo "starting cron"
service cron start

cp /code/Swyft/web_app/order_complition_mail.py /code/Swyft/

gunicorn --timeout 1800 --access-logfile - --workers 3 --bind unix:/code/Swyft/Swyft.sock Swyft.wsgi:application

sleep 10000
