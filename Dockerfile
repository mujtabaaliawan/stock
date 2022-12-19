FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /drf_src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

VOLUME /drf_src

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000



