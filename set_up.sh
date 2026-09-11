#!/bin/bash
python manage.py migrate --noinput
python recreate_superuser.py