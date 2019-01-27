#!/usr/bin/env bash

echo "waiting for postgres"

while ! nc -z users_db 5432; do
    sleep 0.1
done

echo "postgres done"

python manage.py run -h 0.0.0.0
