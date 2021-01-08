FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /var/app/requirements.txt
RUN pip install -r /var/app/requirements.txt

COPY . /var/app/
WORKDIR /var/app/

EXPOSE 8000
