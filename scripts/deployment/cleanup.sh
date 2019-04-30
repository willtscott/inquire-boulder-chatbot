#!/bin/bash

# Run on cloud environment

export ZONE=us-central1-b
export CLUSTER_NAME=bot-cluster
export DEPLOYMENT_NAME=bot-web

kubectl delete deployment bot-web --namespace=default
kubectl delete service bot-web
gcloud config set compute/zone us-central1-b
gcloud container clusters delete bot-cluster 
docker image ls -a
echo "*** Delete docker images ***"
echo "docker image rm [IMAGE_ID]"