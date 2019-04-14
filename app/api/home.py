from flask import Flask, render_template

from app import app


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html");


@app.route('/<string:page_name>')
def render_static(page_name):
    return render_template('%s' % page_name)