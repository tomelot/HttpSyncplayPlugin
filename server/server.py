from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO
from time import time
import json

app = Flask(__name__)
socketio = SocketIO(app)


sync_info = None


@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        content = request.json
        if content:
            global sync_info
            sync_info = content
            socketio.emit('sync', sync_info)
    except Exception as e:
        print(e)
    return ""


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/time')
def get_time():
    return str(time())


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
