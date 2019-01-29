# Docker-Introduction

I used ec2 instance from AWS.

### Docker-image Installation
https://docs.docker.com/machine/install-machine/

base=https://github.com/docker/machine/releases/download/v0.16.0 &&
curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
sudo install /tmp/docker-machine /usr/local/bin/docker-machine

### Docker-compose installation
https://docs.docker.com/compose/install/

### Variables - Optional
```export FLASK_APP=project/__init__.py```

```export FLASK_ENV=development```

### Directory Information
[AirBnB_clone_v1](./AirBnB_clone_v1) - contains my Airbnb_clone_v1 from https://github.com/adrielt07/AirBnB_clone. Added an instruction how to run my Airbnb console using docker container

[first_container](./first_container) - docker orientation tutorial from https://docs.docker.com/get-started/

[testdriven-app](./testdriven-app) - an application I'm currently working on. It serves an API (Python and Flask) and Postgres.

### Run container - Example
1. Ran two terminal windows
2. From terminal 1, change directory to testdriven-app and build the image
```
$ docker-compose -f docker-compose-dev.yml build
$ docker-compose -f docker-compose-dev.yml up -d --build
```
3. From terminal 2, use curl:
```
$ curl 127.0.0.1:5001/users/ping
```

### Issues Encounterd
1. Dangling images - I noticed images, with 'None' tag, are consuming disk space. They are more likely images that are not being referenced or used.

```docker rmi $(docker images -f "dangling=true" -q)```

Some of these images can't be removed because they are being used by an exited container. I have to forcely remove those.

```docker rmi -f $(docker images -f "dangling=true" -q)```

2. Used Container - Just for Personal reference. If I list out all containers, it includes containers that are exited taking up realstate.

```docker container rm $(docker container ls -f status=exited -q)```
