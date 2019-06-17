#!/bin/bash -x

# Run on cloud environment

export PROJECT_ID=inquire-boulder-faq
export IMAGE_NAME=willtscott/inquire-boulder-bot:$TAG_NAME
export NUM_NODES=1
export ZONE=us-central1-b
export CLUSTER_NAME=bot-cluster
export DEPLOYMENT_NAME=bot-web

gcloud config set project $PROJECT_ID
gcloud config set compute/zone $ZONE
gcloud container clusters create $CLUSTER_NAME --num-nodes=$NUM_NODES
kubectl run $DEPLOYMENT_NAME --image=$IMAGE_NAME --port 8080
kubectl expose deployment $DEPLOYMENT_NAME --type=LoadBalancer --port 80 --target-port 8080
sleep 90s
kubectl get service
echo "***Update webhook URL in Dialogflow Fulfilment section with: URL + '/dialog'"
