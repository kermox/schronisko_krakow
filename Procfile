web: gunicorn schronisko_krakow.wsgi
worker: celery -A mails.tasks worker -B --loglevel=info