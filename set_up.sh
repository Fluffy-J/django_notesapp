#!/bin/bash
python manage.py flush --noinput
python recreate_superuser.py