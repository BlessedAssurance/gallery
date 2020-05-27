release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn photo_gallery.wsgi --log-file 