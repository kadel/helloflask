#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from helloflask import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
