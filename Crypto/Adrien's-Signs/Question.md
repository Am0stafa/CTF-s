## The Challenge

You must reverse the encryption function to decrypt the flag given `a`, `p`, and the output of the encryption function.

---
## The Explanation:

This is my understanding of the encryption function:
1. Convert the flag to binary
2. For each bit in the binary representation, generate a random number between 1 and `p`
3. Calculate `n = a^e mod p` which is `a` raised to the power of `e` modulo `p`
4. If the bit is 1, append `n` to the ciphertext
5. If the bit is 0, append `-n mod p` to the ciphertext

## Key Properties Used
1. **Quadratic Residues**:
   - A number n is a quadratic residue mod p if n ≡ x² (mod p) for some x
   - Can be tested using Euler's criterion: n^((p-1)/2) ≡ 1 (mod p)

2. **Special Properties of p**:
   - p ≡ 3 (mod 4) means p = 4k + 3 for some k
   - This makes (-1) a non-quadratic residue mod p
   - Makes computing square roots efficient

3. **Properties of a**:
   - a is chosen to be a quadratic residue mod p
   - All powers of a will also be quadratic residues
   - When negated (-a), becomes non-quadratic residue


---
## The Solution:

To build the decryption function, we need to:
1. Test if a number is a quadratic residue
2. Use the properties of a to decrypt the ciphertext

1. **For Each Ciphertext Number**:
   - Check if it's a quadratic residue mod p
   - If yes → original bit was 1
   - If no → original bit was 0

2. **Bit Collection**:
   - Collect all bits in order
   - Group into bytes (8 bits)
   - Convert to ASCII characters



---