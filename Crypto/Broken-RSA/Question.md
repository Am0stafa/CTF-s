## The Challenge

I tried to send you an important message with RSA, however I messed up my RSA implementation really badly. Can you still recover the flag?

If you think you're doing the right thing but getting garbage, be sure to check all possible solutions.


Challenge files:
  - broken_rsa.txt

---
## The Explanation:

We are given these parameters:
  - `n`: the modulus; very large number
  - `e`: the public exponent; This is unusual and the key weakness!
  - `ct`: the ciphertext; encrypted with the broken RSA!

<br>

Key observation:
  - Normal RSA uses e values like 65537 (prime)
  - Here e = 16 = 2^4 which is very small and a power of 2!
  - This means we can take the 16th root of the ciphertext to get the plaintext!

<br>

Why this RSA is broken?
1. In RSA ct = m^e mod n
2. Here e = 16 = 2^4 which is very small
3. If m^16 < n then ct = m^16 (no modulus reduction occurred!)
4. We can simply take the 16th root of ct to get m!

---
## The Solution:

### Step 1: Understanding the Vulnerability
- In standard RSA, we use a large prime number (typically 65537) as the public exponent 'e'
- Here, e = 16, which is extremely small and a power of 2
- This small exponent creates a critical weakness in the implementation
- When the message is raised to such a small power, it might **not exceed the modulus**

### Step 2: Mathematical Analysis
1. In normal RSA:
   - Encryption: ct = m^e mod n
   - The modulo operation occurs because m^e > n

2. In this broken implementation:
   - If m^16 < n
   - Then ct = m^16 (no modulo needed)
   - This means we have a direct mathematical relationship

### Step 3: Recovery Process
1. Since ct = m^16 (without modulo):
   - We can directly take the 16th root of ct
   - This will give us the original message m
   - No complex RSA decryption needed

2. Implementation considerations:
   - Use a library that can handle large number roots efficiently
   - The root must be exact (no remainder)
   - Convert the resulting number back to bytes to get the flag

### Step 4: Verification
- After taking the 16th root:
  * Check if it's an exact root (no remainder)
  * Convert the number to bytes
  * The result should be readable text (the flag)

### Why This Works
1. The small exponent (e=16) means:
   - The encryption operation might not wrap around modulo n
   - The relationship between m and ct becomes direct
   - No complex factorization or private key needed

2. This vulnerability exists because:
   - The message space was too small relative to n
   - The exponent was too small
   - Both conditions allowed for direct root extraction

### Important Notes
- This type of vulnerability is why RSA implementations:
  * Use large prime numbers for e (typically 65537)
  * Properly pad messages before encryption
  * Follow standardized implementations
- This challenge demonstrates why deviating from standard practices in cryptography can lead to complete system failure

---