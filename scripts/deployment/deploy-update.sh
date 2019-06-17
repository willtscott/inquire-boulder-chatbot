#!/bin/bash -x

# Run build-push locally on new version and then run this script on cloud environment

export IMAGE_NAME=willtscott/inquire-boulder-bot:$TAG_NAME
export DEPLOYMENT_NAME=bot-web

kubectl set image deployment/$DEPLOYMENT_NAME $DEPLOYMENT_NAME=$IMAGE_NAME
kubectl get service
