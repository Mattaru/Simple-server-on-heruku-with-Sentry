import os
import sentry_sdk
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

# Enter your Sentry link here
SENTRY_DSN = 'https://1543850c449c47cc9728989f67816ef2@o453036.ingest.sentry.io/5441339'

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[BottleIntegration()]
)

@route('/')
def im_ok():
    response = HTTPResponse(status=200, body='I am OK')
    return response

@route('/success')
def get_success():
    response = HTTPResponse(status=200, body='OK')
    return response

@route('/fail')
def get_error():
    raise RuntimeError('Server error for the test')

if os.environ.get('SERVER_URL') == 'https://fathomless-escarpment-57347.herokuapp.com':
    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
else:
    run(
        host='localhost',
        port=8080,
        debug=True
    )