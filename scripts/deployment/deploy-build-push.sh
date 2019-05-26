#!/bin/bash -x

# Run in src directory

export IMAGE_NAME=willtscott/inquire-boulder-bot:v3

docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME
# docker run --rm -p 8080:8080 willtscott/inquire-boulder-bot:v1