FROM python:3.10.8

WORKDIR /home/

RUN git clone https://github.com/seoggu/django_corp_web

WORKDIR /home/django_corp_web

RUN pip istall -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

