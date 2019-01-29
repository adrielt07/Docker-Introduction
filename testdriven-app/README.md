### To test the API
1. Ran two terminal windows
2. From terminal 1, ran the following commands:
```
$ docker-compose -f docker-compose-dev.yml build
$ docker-compose -f docker-compose-dev.yml up -d --build
```
3. From terminal 2, use curl:
```
$ curl 127.0.0.1:5001/users/ping
```
