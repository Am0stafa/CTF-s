import socket
import json
from typing import Tuple

def connect_to_server(address: str, port: int) -> socket.socket:
    print(f"[+] Attempting to connect to {address}:{port}")
    s = socket.socket()
    s.connect((address, port))
    print("[+] Connection established successfully")
    return s

def read_until(s: socket.socket, delimiter: bytes) -> bytes:
    print(f"[+] Reading data until delimiter: {delimiter}")
    data = b""
    while not data.endswith(delimiter):
        chunk = s.recv(1)
        data += chunk
        if len(data) % 50 == 0:  # Print progress every 50 bytes
            print(f"[+] Read {len(data)} bytes so far...")
    print(f"[+] Finished reading {len(data)} bytes")
    return data

def receive_json(s: socket.socket) -> dict:
    print("\n[+] Waiting to receive JSON data...")
    data = read_until(s, b'\n')
    print(f"[+] Raw received data: {data}")
    try:
        # Parse the custom format "Key: Value"
        decoded = data.decode().strip()
        key, value = decoded.split(': ', 1)
        # Create a proper JSON-like dictionary
        parsed_data = {key: json.loads(value)}
        print(f"[+] Parsed data: {json.dumps(parsed_data, indent=2)}")
        return parsed_data
    except Exception as e:
        print(f"[-] ERROR: Failed to parse data: {e}")
        raise

def send_json(s: socket.socket, message: dict):
    print(f"\n[+] Sending JSON message: {json.dumps(message, indent=2)}")
    request = json.dumps(message).encode()
    s.sendall(request + b'\n')
    print("[+] Message sent successfully")

def main():
    print("\n=== Starting Roll-your-Own Challenge ===\n")
    
    # Connect to the server
    s = connect_to_server('socket.cryptohack.org', 13403)

    # Step 1: Receive prime q
    print("\n=== Step 1: Receiving prime q ===")
    data = receive_json(s)
    q_hex = data.get('Prime generated')
    q = int(q_hex, 16)
    print(f"[+] Received prime q (hex): {q_hex}")
    print(f"[+] Converted prime q (dec): {q}")

    # Step 2: Choose n and g
    print("\n=== Step 2: Calculating n and g ===")
    n = 15  # Small composite number
    g = 2   # Generator
    print(f"[+] Starting with initial n={n}, g={g}")
    iterations = 0
    while pow(g, q, n) != 1:
        n += 1
        iterations += 1
        if iterations % 100 == 0:
            print(f"[+] Tried {iterations} values for n, current n={n}")
    print(f"[+] Found suitable values: n={n}, g={g}")
    print(f"[+] Verification: g^q mod n = {pow(g, q, n)}")

    # Step 3: Send n and g to server
    print("\n=== Step 3: Sending n and g to server ===")
    payload = {'g': hex(g), 'n': hex(n)}
    send_json(s, payload)

    # Step 4: Receive h
    print("\n=== Step 4: Receiving public key h ===")
    data = receive_json(s)
    h_hex = data.get('Generated my public key')
    h = int(h_hex, 16)
    print(f"[+] Received h (hex): {h_hex}")
    print(f"[+] Converted h (dec): {h}")

    # Step 5: Compute x
    print("\n=== Step 5: Computing x through brute force ===")
    found = False
    for x in range(1, n):
        if x % 100 == 0:
            print(f"[+] Trying x={x}...")
        if pow(g, x, n) == h:
            found = True
            print(f"[+] Found x={x}")
            print(f"[+] Verification: g^x mod n = {pow(g, x, n)} (should equal h={h})")
            break
    
    if not found:
        print("[-] ERROR: Could not find valid x!")
        return

    # Step 6: Send x to server
    print("\n=== Step 6: Sending x to server ===")
    send_json(s, {'x': hex(x)})

    # Step 7: Receive the flag
    print("\n=== Step 7: Receiving final response ===")
    data = receive_json(s)
    print("\n=== Final Result ===")
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[-] ERROR: Script failed with exception: {type(e).__name__}")
        print(f"[-] Error message: {str(e)}")
        raise
