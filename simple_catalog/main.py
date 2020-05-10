#!/usr/bin/env python
from flask import Flask, render_template

from products_views import products_app
from storage import Products


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix='/products/')


@app.route('/')
def index_page(name=None, user_id=None):
    response = render_template(
        'index.html',
        count=len(Products()),
    )
    return response


app.run('localhost', 8080, debug=True)
