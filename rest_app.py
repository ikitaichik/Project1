from flask import Flask, request
from db_connector import *
import os
import signal

app = Flask(__name__)


# supported methods
@app.route('/users/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(id):
    if request.method == 'POST':
        try:
            name = request.json.get('name')
            insert_user(id, name)
            return {'status': 'ok', 'user added': name}, 200  # status code
        except:
            return {'status': 'error', 'reason': "No such id"}, 500 # status code# status cod

    elif request.method == 'GET':
        try:
            name = get_id(id)
            if name == '':
                raise Exception
            else:
                return {'status': 'ok', 'user name': name}, 200
        except:
            return {'status': 'error', 'reason': "No such id"}, 500  # status code

    elif request.method == 'PUT':
        try:
            name = request.json.get('name')
            update_user(name, id)
            return {'status': 'ok', 'user_updated': name}, 200  # status code
        except:
            return {"status": "error", "reason": "No such id"}, 500

    elif request.method == 'DELETE':
        try:
            delete_user(id)
            return {'status': 'ok', 'user_deleted': id}, 200  # status code
        except:
            return {'status': 'error', 'reason': "Mo such id"}, 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5000)