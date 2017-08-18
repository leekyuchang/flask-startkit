# from flask import render_template
from app import app
from flask import request, jsonify

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    return 'This is test page.'

@app.route('/hello')
def hello():
    r = request.get('http://www.google.com')
    return r.text
