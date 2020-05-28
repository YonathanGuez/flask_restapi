# flask RESTful api
Restful Api with python Flask 

## Build Dockerfile :
Base on : https://hub.docker.com/_/python

the dockerfile will build image and install all python dependency with requirements.txt

### Config docker-compose.yml :
my local version of docker-compose
```
$ docker-compose -v
docker-compose version 1.24.1, build 4667896b
```
1) [ref to docker doc ](https://docs.docker.com/compose/compose-file/) I need to use version:'2.2'
2) name of my service : user-registry
3) build my Dockerfile in the current directory we i do docker-compose up : .
4) volumes à créer et à utiliser pour sauvegarder les sources de notre application, 
il doit etre le meme que le WORKDIR de notre Dockerfile: /usr/src/app
5) ports ou acceder a notre server : 5000:80

### Install Dockerfile:
For the first launch and run the code:
```
docker-compose up
```
Windows you need to put IP_OF_DOCKER:5000 , for example:
```
http://192.168.99.100:5000/
```