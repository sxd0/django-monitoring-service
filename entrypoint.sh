#!/bin/sh

echo "Waiting for MySQL..."
while ! nc -z db 3306; do
  sleep 0.5
done
echo "MySQL started"

echo "Waiting for Redis..."
while ! nc -z redis 6379; do
  sleep 0.5
done
echo "Redis started"

if [ ! -f "$DB_APPLIED_MARKER" ]; then
  echo "Applying database migrations..."
  python manage.py migrate
  touch "$DB_APPLIED_MARKER"
  echo "Migrations applied"
fi

exec "$@"