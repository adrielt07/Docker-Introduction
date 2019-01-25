# Docker-Introduction

I used ec2 instance from AWS

To Install Docker-image in Linux:
https://docs.docker.com/machine/install-machine/

base=https://github.com/docker/machine/releases/download/v0.16.0 &&
curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
sudo install /tmp/docker-machine /usr/local/bin/docker-machine
