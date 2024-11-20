## The Challenge

Rearrange the following equations to get the primes \( p, q \):

\[
N = p \cdot q
\]

\[
c_1 = (2 \cdot p + 3 \cdot q)^{e_1} \mod N
\]

\[
c_2 = (5 \cdot p + 7 \cdot q)^{e_2} \mod N
\]

### Challenge files:
- [data.txt](data.txt)

---
## The Explanation:

1. We have a modulus N which is a product of two primes p and q (classic RSA)
2. We have two ciphertext c1 and c2 which are powers of (2p + 3q) and (5p + 7q)
3. The interesting part is that the messages being encrypted are linear combinations of p and q:
    - first message: m1 = 2p + 3q
    - second message: m2 = 5p + 7q
This is a variant of the "Common Modulus Attack" combined with a system of equations.
1. Both equations have the sam`e modulus N
2. We can use the Chinese Remainder Theorem to solve for p and q

---
## The Solution:

<img width="703" alt="Screenshot 2024-11-20 at 10 44 43 PM" src="https://github.com/user-attachments/assets/51e72df0-5656-44b5-9bee-41bc9a7a63fd">



---
