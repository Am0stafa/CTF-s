import socket
import json
import base64
import codecs

HOST = "socket.cryptohack.org"
PORT = 13377

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

def decode_base64(encoded):
    return base64.b64decode(encoded).decode()

def decode_hex(encoded):
    return bytes.fromhex(encoded).decode()

def decode_rot13(encoded):
    return codecs.decode(encoded, 'rot_13')

def decode_bigint(encoded):
    return bytes.fromhex(encoded[2:]).decode()  # Remove '0x' prefix

def decode_utf8(encoded):
    return ''.join(chr(b) for b in encoded)

def decode_message(type, encoded):
    if type == "base64":
        return decode_base64(encoded)
    elif type == "hex":
        return decode_hex(encoded)
    elif type == "rot13":
        return decode_rot13(encoded)
    elif type == "bigint":
        return decode_bigint(encoded)
    elif type == "utf-8":
        return decode_utf8(encoded)
    else:
        raise ValueError(f"Unknown encoding type: {type}")

def main():
    s = connect_socket()
    
    try:
        for _ in range(100):
            received = json_recv(s)
            print(f"Received: {received}")
            
            decoded = decode_message(received["type"], received["encoded"])
            
            to_send = {
                "decoded": decoded
            }
            json_send(s, to_send)
            print(f"Sent: {to_send}")
        
        # After 100 successful decodes, receive the flag
        flag = json_recv(s)
        print(f"Flag: {flag}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        s.close()

if __name__ == "__main__":
    main()
