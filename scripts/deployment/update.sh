#!/bin/bash

# Run build-push locally on new version and then run this script on cloud environment

export IMAGE_NAME=willtscott/inquire-boulder-bot:v2

kubectl set image deployment/bot-web bot-web=willtscott/inquire-boulder-bot:v2