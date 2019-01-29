### Update
Organize the code from v1 using Python Flask

### To test the API
1. Ran two terminal windows
2. From terminal 1, ran the following commands:
```
$ docker-compose -f docker-compose-dev.yml build # Builds the image may take a few minutes at first build
$ docker-compose -f docker-compose-dev.yml up -d --build # Ran and detach the image allowing it to run in the background
$ docker-compose -f docker-compose-dev.yml logs # Checks the log useful for debugging
```
3. From terminal 2, use curl:
```
$ curl 127.0.0.1:5001/users/ping 
# If you get an error - curl: (52) Empty reply from server. Wait for a minute, then ran curl again

$ docker-compose -f docker-compose-dev.yml run users python manage.py test # For unittest
```
