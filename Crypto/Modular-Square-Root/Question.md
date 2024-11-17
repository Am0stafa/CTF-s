## The Challenge

In Legendre Symbol, we introduced a fast way to determine whether a number is a square root modulo a prime. We can go further: there are algorithms for efficiently calculating such roots. The best one in practice is called **Tonelli-Shanks**, which gets its funny name from the fact that it was first described by an Italian in the 19th century and rediscovered independently by Daniel Shanks in the 1970s.

All primes that aren't 2 are of the form `p ≡ 1 mod 4` or `p ≡ 3 mod 4`, since all odd numbers obey these congruences. As the previous challenge hinted, in the `p ≡ 3 mod 4` case, a really simple formula for computing square roots can be derived directly from Fermat's little theorem. That leaves us still with the `p ≡ 1 mod 4` case, so a more general algorithm is required.

In a congruence of the form `r² ≡ a mod p`, Tonelli-Shanks calculates `r`.

> **Note**: Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization - that is, it's a hard problem.

The main use-case for this algorithm is finding elliptic curve coordinates. Its operation is somewhat complex so we're not going to discuss the details, however, implementations are easy to find and Sage has one built-in.

**Task**: Find the square root of `a` modulo the 2048-bit prime `p`. Give the smaller of the two roots as your answer.

**Challenge files**:
- output.txt

---
## The Explanation:

In the previous challenge, we learned:
1. How to check if a number has a square root (using Legendre Symbol)
2. That some numbers have square roots modulo p, and some don't
3. However, the previous challenge didn't fully explain HOW to calculate the square root once we found a quadratic residue.

This New Challenge (Modular Square Root)
This challenge introduces the Tonelli-Shanks algorithm, which is a complete solution for finding square roots in modular arithmetic.

---
## The Solution:

[Your steps to solve the problem goes here step by step explaining each step.]


---