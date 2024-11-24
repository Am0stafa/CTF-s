import os
from random import randint

a = 288260533169915
p = 1007621497415251 # Since p is prime we can use Fermat's Little Theorem to find the inverse

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag]) # Convert flag to binary
    for b in plaintext:
        e = randint(1, p) # Random number between 1 and p
        n = pow(a, e, p) # a^e mod p
        if b == '1':
            ciphertext.append(n) # If the bit is 1, append n
        else:
            n = -n % p
            ciphertext.append(n) # If the bit is 0, append -n mod p
    return ciphertext


# This is a case of the Discrete Logarithm Problem (DLP), where given:
# n (result)
# a (base)
# p (modulus)

from Crypto.Util.number import long_to_bytes

def is_quadratic_residue(n, p):
    """
    Check if n is a quadratic residue modulo p using Euler's criterion
    Returns True if n is a quadratic residue, False otherwise
    """
    return pow(n, (p-1)//2, p) == 1

def decrypt_flag(ciphertext, p):
    """
    Decrypt the flag by checking quadratic residues
    Args:
        ciphertext: List of encrypted values
        p: Prime modulus where p ≡ 3 (mod 4)
    Returns:
        Decrypted flag as bytes
    """
    # Collect bits by checking quadratic residues
    bits = ''
    for n in ciphertext:
        # If n is a quadratic residue, the bit was 1
        # Otherwise, the bit was 0
        bit = '1' if is_quadratic_residue(n, p) else '0'
        bits += bit
    
    # Convert binary string to bytes
    # Process 8 bits at a time to form bytes
    flag_bytes = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        flag_bytes.append(int(byte, 2))
    
    return bytes(flag_bytes)

def main():
    # Given parameters
    p = 1007621497415251  # Prime modulus
    
    # Read encrypted values
    with open('output.txt', 'r') as f:
        ciphertext = eval(f.read())
    
    # Decrypt and print the flag
    flag = decrypt_flag(ciphertext, p)
    print("Decrypted flag:", flag.decode())

if __name__ == "__main__":
    main()