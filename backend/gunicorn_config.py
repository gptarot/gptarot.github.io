# Run: gunicorn -c gunicorn_config.py app:app

import os

workers = 5
max_requests = 1000
timeout = 120

PORT = os.environ.get('PORT', 5000)
bind = f'0.0.0.0:{PORT}'