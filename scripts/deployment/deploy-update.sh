#!/bin/bash

# Run build-push locally on new version and then run this script on cloud environment

export IMAGE_NAME=willtscott/inquire-boulder-bot:v3
export DEPLOYMENT_NAME=bot-web

kubectl set image deployment/$DEPLOYMENT_NAME bot-web=$IMAGE_NAME