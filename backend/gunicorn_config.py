# Run: gunicorn -c gunicorn_config.py wsgi:app

import os

# Gunicorn config variables
workers = 5
worker_class = 'gevent'
preload_app = True
worker_connections = 1000
max_requests = 1000
timeout = 120
backlog = 2048
threads = 2

# Server socket
PORT = os.environ.get('PORT', 5000)
bind = f'0.0.0.0:{PORT}'