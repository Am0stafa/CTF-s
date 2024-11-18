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
# We need to find e (exponent)
# A classic DLP problem

def decrypt_flag(encrypted_values, p):
    """
    Decrypt the flag using quadratic residues
    """
    # Calculate power for quadratic residue check
    power = (p + 1) // 4
    bits = []
    
    for n in encrypted_values:
        # Calculate x = n * (p-n) mod p
        # This gives us a^(2e) mod p
        x = (n * (p - n)) % p
        
        # Calculate the square root using p ≡ 3 (mod 4) property
        sqrt = pow(x, power, p)
        
        # If sqrt equals the original n, it was a positive value (bit 0)
        # If -sqrt equals the original n, it was a negative value (bit 1)
        if sqrt == n:
            bits.append('0')
        elif (p - sqrt) == n:
            bits.append('1')
    
    # Convert bits to bytes
    binary_str = ''.join(bits)
    flag_bytes = []
    
    # Convert each 8 bits to a character
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        flag_bytes.append(int(byte, 2))
    
    return bytes(flag_bytes).decode()




if __name__ == "__main__":
    # Change to the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Read encrypted values
    with open('output.txt', 'r') as f:
        content = f.read()
        encrypted_values = eval(content)

    # Debug: Print first few values and their interpretations
    print("First few encrypted values:")
    for n in encrypted_values[:8]:
        print(f"Value: {n}, {'1' if n > p//2 else '0'}")

    # Decrypt and print the flag
    flag = decrypt_flag(encrypted_values, p)
    print("\nFlag:", flag)
