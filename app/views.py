# from flask import render_template
from app import app

@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def test():
    return 'This is test page.'
