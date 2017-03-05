from datetime import datetime

from app import app
from flask import render_template, jsonify
from flask import request
from flask_socketio import SocketIO, emit
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
@app.route('/', methods=["GET"])
def home():
    return render_template("index_new.jinja2")

@socketio.on('connect', namespace='/test')
def connect_event():
    print('Client connected', request.sid)
    emit('connected')

@socketio.on('disconnect', namespace='/test')
def disconnect_event():
    print('Client disconnected', request.sid)


@socketio.on('ping', namespace='/test')
def ping_pong(message):
    print('pong and message={}'.format(message))
