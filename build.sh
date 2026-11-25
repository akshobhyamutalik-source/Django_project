#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python packages
pip install -r requirements.txt

# Collect static files for WhiteNoise
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
