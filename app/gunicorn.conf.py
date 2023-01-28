bind = '0.0.0.0:80'
worker_class = 'uvicorn.workers.UvicornH11Worker'

workers = 1

# https://github.com/benoitc/gunicorn/pull/862#issuecomment-53175919
max_requests = 500
max_requests_jitter = 200
keepalive = 600

loglevel = 'debug'
