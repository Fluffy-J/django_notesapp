#!/usr/bin/env bash

set -o errexit

python -m pip install --upgrade pip
python -m pip install "pipenv==2026.8.0"

pipenv install --system --deploy

python manage.py collectstatic --noinput
python manage.py migrate --noinput