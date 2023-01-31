import psutil


bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'

workers = 2 * psutil.cpu_count(logical=True) + 1

# https://github.com/benoitc/gunicorn/pull/862#issuecomment-53175919
max_requests = 500
max_requests_jitter = 200

# https://cloud.google.com/load-balancing/docs/https#timeouts_and_retries
keepalive = 620

loglevel = 'debug'
