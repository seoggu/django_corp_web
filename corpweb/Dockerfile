FROM python:3.10.8

WORKDIR /home/

RUN git clone https://github.com/seoggu/django_corp_web.git


WORKDIR /home/django_corp_web

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-gnx5fz4c#(_c-2u$-5#(f(d9@fu88(aal6ns+v(16_mb^%wbb6" > .env

WORKDIR /home/django_corp_web/corpweb

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

