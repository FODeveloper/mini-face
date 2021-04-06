#!/bin/sh

rm -r ./*/migrations
rm ./db.sqlite3

python3 manage.py makemigrations personapp
python3 manage.py makemigrations alertapp
python3 manage.py makemigrations cameraapp
python3 manage.py makemigrations configapp
python3 manage.py migrate
python3 manage.py createsuperuser --username user --email fethiourghi@gmail.com
echo "username is user"
python3 manage.py runserver
