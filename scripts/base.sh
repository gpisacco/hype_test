#!/bin/bash

curl -O https://raw.githubusercontent.com/gpisacco/hype/master/scripts/Dockerfile
docker build -t hype_container .
docker run -d -p 8085:80 hype_container
