#!/bin/bash

# Run on cloud environment

export IMAGE_NAME=willtscott/inquire-boulder-bot:v1
export NUM_NODES=1
export ZONE=us-central1-b
export CLUSTER_NAME=bot-cluster
export DEPLOYMENT_NAME=bot-web

gcloud config set compute/zone us-central1-b
gcloud container clusters create bot-cluster --num-nodes=1
kubectl run bot-web --image=willtscott/inquire-boulder-bot:v1 --port 8080
kubectl expose deployment bot-web --type=LoadBalancer --port 80 --target-port 8080
kubectl get service
echo "***Update webhook URL in Dialogflow Fulfilment section with: URL + '/dialog'"
