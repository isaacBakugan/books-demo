#!/bin/sh

# 1. Salir inmediatamente si un comando falla
set -e

echo "==> [1/3] Aplicando migraciones de base de datos..."
# --noinput evita que Django se quede esperando una respuesta del teclado
python manage.py migrate --noinput

echo "==> [2/3] Recolectando archivos estáticos..."
# Necesario para que el Admin de Django y Whitenoise funcionen en la nube
python manage.py collectstatic --noinput

echo "==> [3/3] Iniciando el servidor Gunicorn..."
# Usamos exec para que Gunicorn reciba las señales de terminación de Docker/GCP
exec gunicorn --bind 0.0.0.0:8080 bookstore_inventory.wsgi:application