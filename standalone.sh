#!/bin/sh

# nohup ./standalone.sh > server.log 2>&1 &


source flask_env/bin/activate
exec gunicorn -b 0.0.0.0:8080 --worker-class gevent --access-logfile - --error-logfile - app:app
