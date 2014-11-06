#!/bin/bash
echo "Starting site..."
celery -A maplecroft worker -l info &
python ./manage.py runserver 0.0.0.0:8000 

echo "Now head over to http://localhost:8000"
