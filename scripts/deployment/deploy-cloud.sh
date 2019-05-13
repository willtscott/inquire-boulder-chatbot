#!/bin/bash

# Run on cloud environment

export IMAGE_NAME=willtscott/inquire-boulder-bot:v3
export NUM_NODES=1
export ZONE=us-central1-b
export CLUSTER_NAME=bot-cluster
export DEPLOYMENT_NAME=bot-web

gcloud config set $ZONE
gcloud container clusters create $CLUSTER_NAME --num-nodes=$NUM_NODES
kubectl run $DEPLOYMENT_NAME --image=$IMAGE_NAME --port 8080
kubectl expose deployment $DEPLOYMENT_NAME --type=LoadBalancer --port 80 --target-port 8080
kubectl get service
echo "***Update webhook URL in Dialogflow Fulfilment section with: URL + '/dialog'"