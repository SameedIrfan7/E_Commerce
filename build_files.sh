#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Collecting static files"
# Collect static files
python manage.py collectstatic --noinput

echo "Making migrations for seller app"
# Make migrations for the seller app
python manage.py makemigrations seller

echo "Migrating the seller app"
# Migrate the seller app
python manage.py migrate seller

echo "Making migrations for buyer app"
# Make migrations for the buyer app
python manage.py makemigrations buyer

echo "Migrating the buyer app"
# Migrate the buyer app
python manage.py migrate buyer

echo "All done!"
