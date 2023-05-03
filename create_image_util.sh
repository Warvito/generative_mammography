#!/bin/bash
#
# A simple script to build the distributed Docker image.
#
# $ create_docker_image.sh
set -ex
TAG=mammography_util

docker build --network=host --tag "aicregistry:5000/${USER}:${TAG}" -f Dockerfile.util . \
  --build-arg USER_ID=$(id -u) \
  --build-arg GROUP_ID=$(id -g) \
  --build-arg USER=${USER}

docker push "aicregistry:5000/${USER}:${TAG}"
