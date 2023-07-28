#!/bin/bash

# This script is used to export the environment variables from the .env file
export $(xargs < .env)

gunicorn --bind "0.0.0.0:$PORT" --workers 5 --timeout 120 api.wsgi:app
