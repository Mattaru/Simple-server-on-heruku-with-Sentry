import os
import sentry_sdk
from bottle import run, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn='https://1543850c449c47cc9728989f67816ef2@o453036.ingest.sentry.io/5441339',
    integrations=[BottleIntegration()]
)

@route('/')
def im_ok():
    return 'Im ok.'

@route('/success')
def get_success():
    return '200'

@route('/fail')
def get_error():
    raise RuntimeError('Server error for the test')
    return '500'

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