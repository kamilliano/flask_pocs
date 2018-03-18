#!/usr/bin/env python

from flask import Flask, jsonify

import lib.code

def create_app():

    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    @app.route('/api')
    def api():

        message = "hello"

        message = lib.code.append_text(message, "calling function from route")

        return message

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=8080, debug=True)