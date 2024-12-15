import socket
import json
import time

def connect_to_server():
    """Establish connection to the server"""
    print("\n[+] Establishing connection to socket.cryptohack.org:13398...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('socket.cryptohack.org', 13398))
    
    # Read welcome message
    welcome = s.recv(4096).decode()
    print(f"[+] Server welcome message: {welcome.strip()}")
    return s

def send_and_receive(sock, bit_index):
    """Send a request for a specific bit and receive response"""
    request = json.dumps({"option": "get_bit", "i": str(bit_index)}).encode() + b'\n'
    sock.send(request)
    response = sock.recv(4096).decode()
    return response

def get_flag():
    s = connect_to_server()
    binary_str = ""
    flag = ""
    total_bits = 8 * 43  # 43 bytes = 344 bits
    
    print("\n[+] Starting timing attack...")
    print("[+] Will process 43 bytes (344 bits)")
    print("[+] Making 10 requests per bit and measuring total time")
    print("[+] If total time > 3500ms: bit is 1, otherwise: bit is 0")
    
    try:
        for i in range(total_bits):
            print(f"\n[*] Processing bit position {i}/{total_bits-1}")
            
            # Make 10 requests and measure total time
            start_time = time.time()
            for j in range(10):
                response = send_and_receive(s, i)
                if j == 0:  # Print first response for debugging
                    pass
            end_time = time.time()
            
            # Calculate total time in milliseconds
            total_time = (end_time - start_time) * 1000
            print(f"[*] Total time for 10 requests: {total_time:.2f}ms")
            
            # Determine bit value based on timing
            if total_time > 3500:
                binary_str += "1"
                print("[*] Time > 3500ms -> Bit is 1")
            else:
                binary_str += "0"
                print("[*] Time <= 3500ms -> Bit is 0")
            
            print(f"[*] Current binary string: {binary_str}")
            
            # Process complete bytes (8 bits)
            if len(binary_str) == 8:
                # Reverse bits before converting to character
                byte_value = int(binary_str[::-1], 2)
                current_char = chr(byte_value)
                flag += current_char
                
                print(f"[+] Completed byte {len(flag)-1:2d}: " +
                      f"binary={binary_str} (reversed={binary_str[::-1]}) " +
                      f"dec={byte_value:3d} char='{current_char}'")
                print(f"[+] Current flag: {flag}")
                
                binary_str = ""  # Reset for next byte
                
    except Exception as e:
        print(f"\n[!] Error occurred: {str(e)}")
    finally:
        print("\n[+] Cleaning up connection...")
        s.close()
    
    if flag:
        print("\n[+] Attack completed!")
        print(f"[+] Final flag: {flag}")
        print(f"[+] Flag length: {len(flag)} bytes")
    else:
        print("\n[!] Failed to retrieve flag")

if __name__ == "__main__":
    print("=== CryptoHack Cofactor Cofantasy Timing Attack ===")
    get_flag()