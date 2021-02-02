import requests


try:
    Message = "Servers were shutdown"
    requests.get('http://127.0.0.1:5000/stop_server')
    requests.get('http://127.0.0.1:5001/stop_server')
except Exception as e:
    print(e)
    Message = "Couldn't shutdown servers"
finally:
    print(Message + poo)

