#!/usr/bin/env bash


./docker/scripts/setup.sh

./docker/scripts/ssh.sh ./manage.py migrate

docker compose up -d
