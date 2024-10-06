def xor_single_byte(data, key):
    return bytes([b ^ key for b in data])

def find_flag(hex_string):
    # Convert hex to bytes
    data = bytes.fromhex(hex_string)
    
    # Try all possible single bytes
    for key in range(256):
        result = xor_single_byte(data, key)
        try:
            decoded = result.decode('utf-8')
            if decoded.startswith('crypto{'):
                return decoded
        except UnicodeDecodeError:
            continue
    
    return "Flag not found"

# The given hex string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

flag = find_flag(hex_string)
print(f"The flag is: {flag}")
