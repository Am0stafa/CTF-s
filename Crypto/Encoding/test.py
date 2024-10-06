import json

def json_send(hsh):
    request = json.dumps(hsh).encode() + b"\n"
    print(request)

json_send({"test": "test"})
