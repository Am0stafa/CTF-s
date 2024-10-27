## The Challenge

Given two prime numbers p = 26513 and q = 32321, use the extended Euclidean algorithm to find integers u and v such that:

p·u + q·v = gcd(p,q)

Enter whichever of u and v is the lower number as the flag.

**Note**: This algorithm will later be crucial for calculating the modular inverse of the public exponent when decrypting RSA ciphertext.

---
## The Explanation:

The Extended Euclidean Algorithm  is a tool that extends the standard Euclidean algorithm for finding the Greatest Common Divisor (GCD) of two numbers. While the standard algorithm just finds the GCD, the extended version goes further by finding the coefficients (u and v) that satisfy Bézout's identity:

p·u + q·v = gcd(p,q)

Why care?

This is particularly important in cryptography for several reasons:

1. **Finding Modular Multiplicative Inverses**: 
   - When working with prime numbers, their GCD is always 1
   - This means we can find values u and v where: p·u + q·v = 1
   - These values are essential for calculating **modular inverses**

2. **RSA Cryptography Application**:
   - In RSA encryption/decryption, we need to find the modular multiplicative inverse of the public exponent
   - The EEA provides an efficient way to calculate this inverse
   - Without this algorithm, RSA decryption would not be practical

3. **Properties with Prime Numbers**:
   - When p and q are prime, they are coprime
   - This means their GCD is always 1
   - Therefore, we're finding u and v where: p·u + q·v = 1
   - At least one of these values (u or v) will be negative


---
## The Solution:

To solve this challenge, I have implemented the Extended Euclidean Algorithm by following 

---