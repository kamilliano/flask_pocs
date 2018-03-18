#!/usr/bin/env python

from flask import Flask

import lib.code

app = Flask(__name__)

@app.route('/')
def index():

    message = "hello"

    message = lib.code.append_text(message, " calling function from route")

    return message

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)