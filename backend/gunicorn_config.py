# Run: gunicorn -c gunicorn_config.py app:app

import os, multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 1000
timeout = 120

PORT = os.environ.get('PORT', 5000)
bind = f'0.0.0.0:{PORT}'