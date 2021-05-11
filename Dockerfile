FROM python:3.8.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

RUN apt-get update && apt-get install -y 
RUN apt-get install libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit nginx gunicorn cron nano -y

WORKDIR /code



COPY ./requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt && pip install django-crispy-forms && pip install gunicorn
COPY myproject-nginx.conf /etc/nginx/sites-enabled/


COPY . /code/


EXPOSE 8000 80
CMD ["./entrypoint.sh"]
