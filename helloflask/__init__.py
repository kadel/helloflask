# -*- coding: utf-8 -*-
import os

import flask
import redis
import os

app = flask.Flask(__name__)
app.config['DEBUG'] = False


@app.route('/')
def index():

    redis_master_host = os.getenv('REDIS_MASTER_PORT_6379_TCP_ADDR')
    redis_master_port = os.getenv('REDIS_MASTER_PORT_6379_TCP_PORT')

    redis_slave_host = os.getenv('REDIS_SLAVE_PORT_6379_TCP_ADDR')
    redis_slave_port = os.getenv('REDIS_SLAVE_PORT_6379_TCP_PORT')

    r_master = redis.StrictRedis(host=redis_master_host, port=redis_master_port)

    counter_master = r_master.incr('counter')

    # connect to slave only if slave was configured
    if redis_slave_host and redis_slave_port:
        r_slave = redis.StrictRedis(host=redis_slave_host, port=redis_slave_port)
        counter_slave = r_slave.get('counter')
    else:
        counter_slave = None


    return flask.render_template('index.html',
                                 counter_master=counter_master,
                                 counter_slave=counter_slave)
