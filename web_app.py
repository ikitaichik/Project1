from flask import Flask
from db_connector import *
import os
import signal

app = Flask(__name__)


@app.route('/users/get_user_data/<id>')
def user(id):
    try:
        name = get_id(id)
        if name == '':
            return "<H1 id='error'>""No such user: " + id + "</H1>", 500
        else:
            return "<H1 id='user'>" + name + "</H1>", 200
    except:
        return "<H1 id='error'>""Something went wrong...</H1>", 500


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5001)
