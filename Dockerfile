# base image
FROM python:3.10

# setup environment variable
ENV DockerHOME=/home/app/paymob-challenge
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

# install dependencies
RUN pip install --upgrade pip

# copy whole project to docker home directory.
COPY . $DockerHOME

# install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# start server
CMD python minisearch/manage.py runserver 0.0.0.0:8000
