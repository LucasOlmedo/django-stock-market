#!/bin/sh

# Check if manage.py exists
if [ -f "manage.py" ]; then
    echo "manage.py found. Starting Django server..."
    python manage.py runserver 0.0.0.0:8000
else
    echo "manage.py not found. Creating Django project..."
    django-admin startproject core .
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi
