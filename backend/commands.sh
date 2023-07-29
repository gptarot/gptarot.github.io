#!/bin/bash

# Check if the .env file exists
if [ -f ".env" ]; then
    # Export the environment variables from the .env file
    export $(xargs < .env)
else
    echo "Proceeding without .env. Please make sure to set the environment variables manually on Railway."
fi

# Run the gunicorn server
gunicorn --bind "0.0.0.0:$PORT" --workers 5 --timeout 120 api.wsgi:app