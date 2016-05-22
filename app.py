#!/usr/bin/env python

import os
import socket
import logging

from bottle import route, request, response, error, default_app, view, static_file, template, hook
from tinydb import TinyDB, Query
from tinydb.operations import increment

def return_tpl(tpl, *data):
    if not appMode is 'prod':
        response.code = '403'
        return template("maintain/index", *data)
    else:
        return template(tpl, *data)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='views/static')

@route('/')
def index():
    return return_tpl('home')

if __name__ == '__main__':

    app = default_app()
    
    appReload = bool(os.getenv('APP_RELOAD', False))
    appSecret = os.getenv('APP_SECRET', '')
    appMode = os.getenv('APP_MODE', 'prod')
    
    serverHost = os.getenv('IP', 'localhost')
    serverPort = os.getenv('PORT', '5000')

    mailgunToken = os.getenv('MAILGUN_TOKEN', '')

    # Now we're ready, so start the server
    # Instantiate the logger
    log = logging.getLogger('log')
    console = logging.StreamHandler()
    log.setLevel(logging.INFO)
    log.addHandler(console)

    if appSecret == '':
        log.error(
            'Secure tokens disabled, using empty secret. Set APP_SECRET to secure seed and restart.'
        )

    if mailgunToken == '':
        log.error(
            'Unable to connect to mailgun API. Inbound and outbound sending will be disabled.'
        )

    # Instantiate a connection to the database
    db = TinyDB(os.getenv('APP_DATABASE', 'db/app.json'))
    
    # Now we're ready, so start the server
    try:
        log.info("Successfully started application server on " + socket.gethostname())
        app.run(host=serverHost, port=serverPort, reloader=bool(appReload))
    except:
        log.error("Failed to start application server on " + socket.gethostname())