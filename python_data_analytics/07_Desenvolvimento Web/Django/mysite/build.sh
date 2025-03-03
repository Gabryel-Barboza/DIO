#!/usr/bin/env bash
# Exit on error
set -o errexit

poetry install --no-root --without dev

# Coletar arquivos estáticos
python manage.py collectstatic --no-input

python manage.py migrate

# Criar superuser de variáveis ambiente
# DJANGO_SUPERUSER_{EMAIL|PASSWORD|USERNAME}
# -> python manage.py createsuperuser --no-input
