#!/usr/bin/env bash

docker build -t datawave/templater:latest --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .
