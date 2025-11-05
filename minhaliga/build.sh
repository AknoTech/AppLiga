#!/usr/bin/env bash
# Sair se um comando falhar
set -o errexit

# 1. Instalar os pacotes da nossa "lista de compras"
pip install -r requirements.txt

# 2. Coletar os arquivos estáticos (CSS/JS do painel admin)
python manage.py collectstatic --no-input

# 3. Rodar as migrações (criar/atualizar as tabelas do banco)
python manage.py migrate