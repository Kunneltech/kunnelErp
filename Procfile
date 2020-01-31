web: gunicorn pro1.wsgi --log-file -

release: python manage.py migrate
web: run-program waitress-serve --port=$PORT settings.wsgi:application
