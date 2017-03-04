from datetime import datetime

from app import app
from flask import render_template, jsonify
from flask import request
from flask_socketio import SocketIO, emit
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
@app.route('/', methods=["GET"])
def home():
    return render_template("index.jinja2")

@socketio.on('my_ping', namespace='/test')
def ping_pong():
        emit('my_pong')
