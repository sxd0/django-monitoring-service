#!/bin/sh

echo "подождать mysql"
while ! nc -z db 3306; do
  sleep 0.5
done
echo "mysql стартанул"

echo "подождать редис"
while ! nc -z redis 6379; do
  sleep 0.5
done
echo "редис запущен"

if [ ! -f "$DB_APPLIED_MARKER" ]; then
  echo "миграции"
  python manage.py migrate
  touch "$DB_APPLIED_MARKER"
  echo "миграции применены"
fi

exec "$@"