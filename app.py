#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is home page.'

@app.route('/info')
def info():
    return 'This is info page.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
