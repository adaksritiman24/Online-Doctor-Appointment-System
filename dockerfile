FROM python:3.9

COPY . /odas_app

WORKDIR /odas_app

CMD pip install -r requirements.txt && cd ./odas && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
