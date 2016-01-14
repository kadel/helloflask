# -*- coding: utf-8 -*-
import os

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return flask.render_template('index.html')
