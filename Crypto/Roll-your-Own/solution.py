import socket
import json

def recv_line(s):
    data = b""
    while not data.endswith(b"\n"):
        chunk = s.recv(1)
        if not chunk:
            break
        data += chunk
    return data

def clean_hex_string(hex_str):
    """Clean hex string by removing quotes and ensuring 0x prefix"""
    hex_str = hex_str.strip().strip('"\'')
    if not hex_str.startswith('0x'):
        hex_str = '0x' + hex_str
    return hex_str

def main():
    print("\n=== Roll Your Own Discrete Log Challenge ===\n")
    
    host = "socket.cryptohack.org"
    port = 13403
    
    print(f"[+] Connecting to {host}:{port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[+] Connected successfully!\n")

    try:
        # Receive initial prime q
        line = recv_line(s).decode().strip()
        print(f"[+] Raw server response: {line}")
        
        try:
            q_hex = line.split(": ")[1]
            q_hex = clean_hex_string(q_hex)
            q = int(q_hex, 16)
            print(f"[+] Received prime q from server:")
            print(f"    - Hex: {q_hex}")
            print(f"    - Decimal: {q}")
            print(f"    - Bit length: {q.bit_length()} bits\n")
        except (IndexError, ValueError) as e:
            print(f"[!] Error parsing prime q: {e}")
            raise

        # Calculate our parameters g and n
        print("[+] Calculating parameters g and n...")
        print("    Strategy:")
        print("    - Choose g = q + 1")
        print("    - Choose n = q^2")
        print("    This ensures pow(g,q,n) = 1 because:")
        print("    - g^q mod n = (q+1)^q mod q^2")
        print("    - When expanded, all terms except 1 will be multiples of q^2")
        print("    - Therefore, g^q mod n = 1\n")
        
        g = q + 1
        n = q * q

        print(f"[+] Calculated parameters:")
        print(f"    g = {g}")
        print(f"    n = {n}\n")

        before_input_line = recv_line(s).decode().strip()
        print(f"[+] Server prompt: {before_input_line}")
        
        params = {"g": hex(g), "n": hex(n)}
        params_json = json.dumps(params)
        print("[+] Sending parameters to server:")
        print(f"    {json.dumps(params, indent=4)}\n")
        s.send((params_json + "\n").encode())

        # Receive public key h
        line = recv_line(s).decode().strip()
        print(f"[+] Raw server response: {line}")
        
        try:
            h_hex = line.split(": ")[1]
            h_hex = clean_hex_string(h_hex)
            h = int(h_hex, 16)
            print(f"[+] Received server's public key h:")
            print(f"    - Hex: {h_hex}")
            print(f"    - Decimal: {h}\n")
        except (IndexError, ValueError) as e:
            print(f"[!] Error parsing public key h: {e}")
            raise

        # Compute private key x
        print("[+] Computing server's private key x...")
        print("    Strategy:")
        print("    - Since h = g^x mod n")
        print("    - And g = q + 1")
        print("    - h = (q+1)^x mod q^2")
        print("    - When x < q, this simplifies to: h = 1 + qx mod q^2")
        print("    - Therefore, x = (h-1)/q\n")
        
        x = (h - 1) // q
        print(f"[+] Computed private key x = {x}\n")

        before_input_line = recv_line(s).decode().strip()
        print(f"[+] Server prompt: {before_input_line}")
        
        answer = {"x": hex(x)}
        answer_json = json.dumps(answer)
        print("[+] Sending answer to server:")
        print(f"    {json.dumps(answer, indent=4)}\n")
        s.send((answer_json + "\n").encode())

        # Receive final response
        line = recv_line(s).decode().strip()
        try:
            response = json.loads(line)
            print("[+] Server response:")
            print(f"    {json.dumps(response, indent=4)}\n")
            
            if "flag" in response:
                print("[+] Successfully retrieved flag!")
                print(f"[+] Flag: {response['flag']}")
            elif "error" in response:
                print(f"[!] Server returned error: {response['error']}")
            
        except json.JSONDecodeError as e:
            print(f"[!] Error parsing server response: {e}")
            print(f"[!] Raw response: {line}")

    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        s.close()
        print("[+] Connection closed")

if __name__ == "__main__":
    main()
