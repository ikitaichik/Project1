import requests


def get(id):
    try:
        res = requests.get(f"http://127.0.0.1:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")


def post(id, name):
    try:
        res = requests.post(f"http://127.0.0.1:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")


def put(id, name):
    try:
        res = requests.put(f"http://127.0.0.1:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")


def delete(id):
    try:
        res = requests.delete(f"http://127.0.0.1:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")









