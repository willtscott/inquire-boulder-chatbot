#!/bin/bash

# Run in src directory

export IMAGE_NAME=willtscott/inquire-boulder-bot:v1

docker build -t willtscott/inquire-boulder-bot:v1 .
docker push willtscott/inquire-boulder-bot:v1
# docker run --rm -p 8080:8080 willtscott/inquire-boulder-bot:v1