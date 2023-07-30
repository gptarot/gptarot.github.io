# Run: gunicorn -c gunicorn_config.py app:app

import os

# Gunicorn config variables
workers = 5
max_requests = 1000
timeout = 120
backlog = 2048
threads = 2

# Server socket
PORT = os.environ.get('PORT', 5000)
bind = f'0.0.0.0:{PORT}'

# Choose gevent worker type
worker_class = 'gevent'