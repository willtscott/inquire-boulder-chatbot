#!/bin/bash -x

# Run on cloud environment

export ZONE=us-central1-b
export CLUSTER_NAME=bot-cluster
export DEPLOYMENT_NAME=bot-web

kubectl delete deployment $DEPLOYMENT_NAME --namespace=default
kubectl delete service $DEPLOYMENT_NAME
gcloud config set compute/zone $ZONE
gcloud container clusters delete $CLUSTER_NAME 
docker image ls -a
echo "*** Delete docker images ***"
echo "docker image rm [IMAGE_ID]"
