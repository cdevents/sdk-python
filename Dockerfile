# syntax=docker/dockerfile:1

FROM python:3.8

# Setup environment
RUN apt-get update && apt-get install -y \
    python3-distutils \
    build-essential

# Copy requirements
COPY ./requirements ./requirements

# Installing requirements
RUN pip install -r ./requirements

# Copy needed files (see .dockerignore for what will be included)
COPY . /cdevents-client

WORKDIR /cdevents-client

# Build
RUN /bin/bash -c "make package-install"

WORKDIR /cdevents-client
