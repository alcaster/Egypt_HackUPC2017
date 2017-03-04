from datetime import datetime

from app import app
from flask import render_template, jsonify
from flask import request


@app.route('/', methods=["GET"])
def home():
    return render_template("index.jinja2")

