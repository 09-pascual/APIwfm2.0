#!/bin/bash

rm db.sqlite3
rm -rf ./wfmapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations wfmapi
python3 manage.py migrate wfmapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

