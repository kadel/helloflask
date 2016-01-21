# -*- coding: utf-8 -*-
import os

import flask
import redis
import os

app = flask.Flask(__name__)
app.config['DEBUG'] = False


@app.route('/')
def index():

    r = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), db=0)
    counter = r.incr('counter')
    return flask.render_template('index.html', counter=counter)
