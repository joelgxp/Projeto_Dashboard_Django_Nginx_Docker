#!/bin/sh
#python manage.py migrate --no-input
gunicorn base.wsgi:application --bind 0.0.0.0:8000