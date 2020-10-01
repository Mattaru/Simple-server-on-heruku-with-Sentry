import os
import sentry_sdk
from bottle import run, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_dsn = 'enter your link'

sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[BottleIntegration()]
)

@route('/')
def im_ok():
    return 'Im ok.'

@route('/success')
def get_success():
    return '200 OK'

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