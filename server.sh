#!/bin/sh

if [ -z "$PORT"]
then
  PORT=5005
fi

rasa run --endpoints endpoints.yml --credentials credentials.yml