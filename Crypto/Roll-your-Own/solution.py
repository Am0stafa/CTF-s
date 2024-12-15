import socket
import json

def recv_line(s):
    """Receive a line from the socket with status indicator"""
    print("[*] Waiting for server response...", end='\r')
    data = b""
    while not data.endswith(b"\n"):
        chunk = s.recv(1)
        if not chunk:
            break
        data += chunk
    print("[+] Received server response    ")  # Clear the waiting message
    return data

def verify_params(g, q, n):
    """Verify that our parameters satisfy the server's requirements"""
    if g < 2:
        return False, "g must be >= 2"
    if n < 2:
        return False, "n must be >= 2"
    if pow(g, q, n) != 1:
        return False, "pow(g,q,n) must equal 1"
    return True, "Parameters valid"

def main():
    print("\n=== Roll Your Own Discrete Log Challenge ===\n")
    
    host = "socket.cryptohack.org"
    port = 13403
    
    print(f"[+] Connecting to {host}:{port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[+] Connected successfully!\n")

    try:
        # Get prime q
        line = recv_line(s).decode().strip()
        if "Prime generated:" not in line:
            raise ValueError(f"Expected prime, got: {line}")
        
        q_hex = line.split("Prime generated:")[1].strip().strip('"')
        q = int(q_hex, 16)
        print(f"[+] Received prime q:")
        print(f"    - Hex: 0x{q:x}")
        print(f"    - Decimal: {q}")
        print(f"    - Bit length: {q.bit_length()} bits\n")

        # Calculate and verify parameters
        print("[+] Calculating parameters g and n...")
        g = q + 1
        n = q * q
        
        valid, msg = verify_params(g, q, n)
        if not valid:
            raise ValueError(f"Parameter validation failed: {msg}")
        
        print("[+] Parameters verified:")
        print(f"    g = {g}")
        print(f"    n = {n}")
        print(f"    pow(g,q,n) = {pow(g,q,n)}\n")

        # Send parameters immediately
        params = {
            "g": f"0x{g:x}",
            "n": f"0x{n:x}"
        }
        
        print("[+] Sending parameters:")
        print(json.dumps(params, indent=4))
        s.send((json.dumps(params) + "\n").encode())
        print("[+] Parameters sent\n")

        # Get public key
        print("[*] Waiting for public key...")
        line = recv_line(s).decode().strip()
        if "Generated my public key:" not in line:
            raise ValueError(f"Expected public key, got: {line}")
        
        h_hex = line.split("Generated my public key:")[1].strip().strip('"')
        h = int(h_hex, 16)
        print(f"[+] Received public key h:")
        print(f"    - Hex: 0x{h:x}")
        print(f"    - Decimal: {h}\n")

        # Calculate private key
        print("[+] Computing private key...")
        x = (h - 1) // q
        print(f"[+] Computed x = {x}")
        
        # Verify our solution
        computed_h = pow(g, x, n)
        if computed_h != h:
            raise ValueError(f"Solution verification failed: {computed_h} != {h}")
        print("[+] Solution verified: pow(g,x,n) == h\n")

        # Send solution
        answer = {"x": f"0x{x:x}"}
        print("[+] Sending solution:")
        print(json.dumps(answer, indent=4))
        s.send((json.dumps(answer) + "\n").encode())
        print("[+] Solution sent\n")

        # Get flag
        print("[*] Waiting for flag...")
        response = recv_line(s).decode().strip()
        try:
            result = json.loads(response)
            if "flag" in result:
                print(f"[+] Success! Flag: {result['flag']}")
            elif "error" in result:
                print(f"[!] Server error: {result['error']}")
            else:
                print(f"[!] Unexpected response: {response}")
        except json.JSONDecodeError:
            print(f"[!] Failed to parse response: {response}")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        s.close()
        print("\n[+] Connection closed")

if __name__ == "__main__":
    main()
