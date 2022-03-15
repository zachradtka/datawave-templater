#!/usr/bin/env bash

docker run --rm -v $(pwd)/data:/data datawave/templater:latest /data/templates /data/output