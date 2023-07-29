#!/bin/bash

# Check if the .env file exists
if [ -f ".env" ]; then
    # Export the environment variables from the .env file
    export $(xargs < .env)
else
    echo "WARNING: .env file not found. Proceeding without it. Please make sure to set the environment variables manually."
fi

# Run the gunicorn server
gunicorn --bind "0.0.0.0:$PORT" --workers 5 --timeout 120 api.wsgi:app