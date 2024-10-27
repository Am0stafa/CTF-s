## The Challenge

The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a, b).

For example:
- When a = 12, b = 8, the divisors of a are {1, 2, 3, 4, 6, 12} and the divisors of b are {1, 2, 4, 8}. Comparing these two, we see that gcd(a, b) = 4.
- When a = 11, b = 17, both numbers are prime. Since prime numbers have only themselves and 1 as divisors, gcd(a, b) = 1.

We say that for any two integers a, b, if gcd(a, b) = 1 then a and b are coprime integers.

Important properties:
- If a and b are prime, they are also coprime
- If a is prime and b < a then a and b are coprime
- Think about why this is not necessarily true when a is prime and b > a

Your task:
1. Implement Euclid's Algorithm to calculate the GCD of two numbers
2. Use your implementation to find gcd(66528, 52920)

---
## The Explanation:


First I want to explain what coprime numbers are:
### Understanding Coprime Numbers

Two numbers are considered **coprime** (or relatively prime) when their greatest common divisor (GCD) equals 1. This means that the only positive number that divides both numbers evenly is 1, basically, two prime numbers. For example:
- 15 and 28 are coprime because they share no common factors except 1
- 15 = 3 × 5
- 28 = 2² × 7
- Their factors have no overlap, so gcd(15, 28) = 1

This concept is crucial in cryptography because:
- It is fundamental to algorithms like RSA  because if the public exponent e is not coprime to φ(n), the encryption becomes impossible to decrypt uniquely.

### Euclid's Algorithm Explained

Euclid's Algorithm is an efficient method for finding the GCD of two numbers. Here is how it works:
- The GCD of two numbers also divides their difference
- We can keep reducing the problem to smaller numbers until we find the GCD

Here's how it works step by step:
1. Start with two numbers a and b
2. Divide a by b to get a quotient q and remainder r
   - a = b × q + r
3. If r = 0, then b is the GCD
4. If r ≠ 0, then gcd(a,b) = gcd(b,r)
5. Repeat the process using b as the new a and r as the new b

For example, let's find gcd(48, 18):
48 = 18 × 2 + 12    (a = b × 2 + 12)
18 = 12 × 1 + 6     (b = 12 × 1 + 6)
12 = 6 × 2 + 0      (12 = 6 × 2 + 0)

Since we got a remainder of 0, the GCD is 6.

This algorithm is efficient because:
- It reduces the numbers in each step
- It requires no factorization
- It works with any positive integers
- It has a logarithmic time complexity relative to the input numbers

---

## The Solution:

### Implementation Overview
My implementation of Euclid's Algorithm is using both binary operations and efficient modular arithmetic. This implementation combines classical algorithmic optimization with binary operations as optimizations.
