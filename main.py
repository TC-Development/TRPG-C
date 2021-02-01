import flask
from flask_socketio import SocketIO
app = flask.Flask("UniversalTRPGPlatform")

socket=SocketIO(app,async_mode="eventlet",logger=True)

@app.route('/')
def hello_world():
    return 'Hello, UTP!'