import os
import multiprocessing

workers = int(os.environ.get('GUNICORN_PROCESSES', multiprocessing.cpu_count()))
threads = int(os.environ.get('GUNICORN_THREADS', '7'))
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '300'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }