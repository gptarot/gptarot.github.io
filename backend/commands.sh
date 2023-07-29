#!/bin/bash

# Check if the .env file exists
if [ -f ".env" ]; then
    # Export the environment variables from the .env file
    export $(xargs < .env)
else
    echo "CLOUD WARNING: Proceeding without .env. Please make sure to set the environment variables manually."
fi

# Run the gunicorn server
gunicorn -c gunicorn_config.py api.wsgi:app