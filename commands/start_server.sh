#!/bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py runserver 0:8000