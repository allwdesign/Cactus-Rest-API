# Which image to use as the base, container will work on python 3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update; apt-get --assume-yes install binutils libproj-dev gdal-bin gettext postgresql-client netcat htop lsof telnet

# This sets the working directory in which my application will be launched.
RUN mkdir /code

WORKDIR /code

# Copy all the code from the project folder to the directory in the container.
ADD . /code/

# Install dependencies.
RUN pip install -r /code/requirements/dev.txt

