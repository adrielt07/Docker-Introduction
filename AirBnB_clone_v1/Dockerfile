# base image
FROM python:3.6.5-alpine

# set working directory
WORKDIR /usr/src/app

# add everything in the current location to /usr/src/app/
COPY . /usr/src/app

# run server
CMD ["python3", "/usr/src/app/console.py"]
