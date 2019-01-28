# Docker-Introduction

I used ec2 instance from AWS.

### Docker-image Installation
https://docs.docker.com/machine/install-machine/

base=https://github.com/docker/machine/releases/download/v0.16.0 &&
curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
sudo install /tmp/docker-machine /usr/local/bin/docker-machine

### Docker-compose installation
https://docs.docker.com/compose/install/

### Variables
```export FLASK_APP=project/__init__.py```

```export FLASK_ENV=development```

### Run container
1. Change directory to testdriven-app
```
$ docker-compose -f docker-compose-dev.yml build
$ docker-compose -f docker-compose-dev.yml up -d --build
```
