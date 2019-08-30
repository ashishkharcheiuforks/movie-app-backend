#!/bin/bash

# Migrate all migration files, not migrated
python manage.py migrate

# Compile translation files
python manage.py compilemessages -l tr
python manage.py compilemessages -l en
