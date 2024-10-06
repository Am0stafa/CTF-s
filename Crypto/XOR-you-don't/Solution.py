from itertools import cycle

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Known start of the flag
known_start = b"crypto{"

# Ciphertext in hex
cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert ciphertext from hex to bytes
cipher_bytes = bytes.fromhex(cipher_hex)

# XOR the first 7 bytes of ciphertext with known start to get part of the key
partial_key = xor_bytes(cipher_bytes[:7], known_start)

print(f"Partial key: {partial_key}")

# Try to guess the last byte of the key (assuming it's a readable character)
for last_byte in range(256):
    potential_key = partial_key + bytes([last_byte])
    decrypted = xor_bytes(cipher_bytes, cycle(potential_key))
    
    if all(32 <= byte <= 126 for byte in decrypted):  # Check if all characters are printable ASCII
        print(f"Potential full key: {potential_key}")
        print(f"Decrypted message: {decrypted.decode('ascii')}")
        break
else:
    print("Couldn't find a valid key.")