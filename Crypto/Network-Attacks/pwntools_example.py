import socket
import json

HOST = "socket.cryptohack.org"
PORT = 11112

def connect_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def json_recv(s):
    data = b""
    while not data.endswith(b"\n"):
        data += s.recv(1)
    return json.loads(data.decode())

def json_send(s, hsh):
    request = json.dumps(hsh).encode() + b"\n"
    s.sendall(request)

def main():
    s = connect_socket()

    # Receive and print initial messages
    for _ in range(1):
        print(s.recv(1024).decode().strip())

    # Send the request
    request = {
        "buy": "flag"
    }
    
    json_send(s, request)

    # Receive and print the response
    response = json_recv(s)
    print(response)

    s.close()

if __name__ == "__main__":
    main()
