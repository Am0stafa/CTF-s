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

The challenge gives us a modulus N = p * q (product of two primes)

We are also given two ciphertexts c1 and c2 which are powers of (2p + 3q) and (5p + 7q)


---
## The Solution:

1. **Key Transformation**:
   We create new variables:
   ```
   g₁ = c₁^e₂ ≡ (2p + 3q)^(e₁e₂) mod N
   g₂ = c₂^e₁ ≡ (5p + 7q)^(e₁e₂) mod N
   ```

2. **Binomial Property**:
   When working modulo q:
   ```
   g₁ ≡ (2p)^(e₁e₂) mod q  (because 3q ≡ 0 mod q)
   g₂ ≡ (5p)^(e₁e₂) mod q  (because 7q ≡ 0 mod q)
   ```

3. **Clever Combination**:
   Define D = 5^(e₁e₂)g₁ - 2^(e₁e₂)g₂
   - This is divisible by q
   - Therefore, q = gcd(D, N)

## Why This Works

1. **Modular Properties**:
   - When working mod q, any term with q becomes 0
   - This simplifies our expressions significantly

2. **The Magic of D**:
   - D = 5^(e₁e₂)g₁ - 2^(e₁e₂)g₂
   - Mod q, this becomes:
     ```
     D ≡ 5^(e₁e₂)(2p)^(e₁e₂) - 2^(e₁e₂)(5p)^(e₁e₂) ≡ 0 (mod q)
     ```
   - Therefore, q must divide D

3. **Finding q**:
   - Since q divides both D and N
   - q = gcd(D, N) gives us one of our prime factors

This solution is elegant because it:
1. Uses properties of modular arithmetic cleverly
2. Avoids complex root-finding
3. Reduces to a simple GCD computation
4. Works efficiently even with large numbers

The key insight is transforming the problem from solving complex modular equations to finding a GCD, which is computationally efficient.

---
