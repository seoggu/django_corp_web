FROM python:3.10.8

RUN apt-get -y update
RUN apt-get -y install vim

WORKDIR /home/
RUN mkdir /django_corp_web

ADD . /home/django_corp_web/corpweb

WORKDIR /home/django_corp_web/corpweb/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && gunicorn corpweb.wsgi --bind 0.0.0.0:8000"]


