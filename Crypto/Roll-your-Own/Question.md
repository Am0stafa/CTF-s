## The Challenge

Cracking discrete logarithms is hard. Change my mind. I'll even let you to use your own parameters, as long as the modulus is of the given order.

Connect at socket.cryptohack.org 13403

Challenge files:
  - 13403.py


---
## The Explanation:

Looking at the challenge code:
  1. Server generates a 512-bit prime `q`
  2. Server expect us to provide a value `g` and `n`
  3. These must satisfy `pow(g, q, n) = 1`
  4. Server generates a random integer `x` and computes `h = g^x mod n`
  5. We need to find `x` to get the flag
**Thats a typical Diffie-Hellman key exchange!**
**Discrete logarithms problem?**

<br>

Key observation:
  - We choose our own `g` and `n`
  - The condition `g^q mod n = 1` is crucial
  - This means that `g` is a generator of the cyclic group of order `q`
  - **If we choose the parameters carefully we can make the DLP easy to solve!**

---
## The Solution:

### Step 1: Understanding the Vulnerability
The key weakness in this challenge is that we can choose our own parameters `g` and `n`. While normally the Discrete Logarithm Problem is hard, we can make it trivially easy by choosing specific values.

Instead of trying to find g where pow(g,q,n)=1, we can use the fact that for a prime modulus p, we know that:
pow(g, p-1, p) = 1 (Fermat's Little Theorem)

### Step 2: Clever Parameter Selection
1. **Choosing n**:
   - We set `n = q + 1` where q is the prime from the server
   - Why? Because in modular arithmetic mod (q+1):
     * Any number raised to power q will equal 1
     * This creates a very simple cyclic group structure
     * This satisfies the server's requirement that g^q ≡ 1 (mod n)

2. **Choosing g**:
   - We select g = 2 (a small number)
   - Why? Because:
     * Small generators make discrete logarithm computation easier
     * 2 is primitive enough for our purposes
     * The values stay manageable throughout calculations

### Step 3: Mathematical Reasoning
1. **Group Structure**:
   - When n = q + 1:
     * The multiplicative group has order q
     * All elements have order dividing q
     * This creates a very predictable pattern

2. **Why It Works**:
   - In normal DLP: finding x in g^x ≡ h (mod n) is hard
   - In our setup:
     * The group structure is simplified
     * The values cycle in a predictable way
     * The discrete logarithm becomes a simple counting problem

### Step 4: Finding the Secret
1. **Computing x**:
   - When server sends h = g^x mod n:
     * Since g = 2, h is just 2^x mod (q+1)
     * We can find x by counting how many times we need to multiply by 2
     * This is much easier than solving a general DLP

2. **Efficiency**:
   - With these parameters:
     * No need for complex algorithms like baby-step giant-step
     * Simple multiplication and counting suffices
     * The solution space is manageable

### Breaking the DLP Step by Step:

1. **Our Parameter Setup**:
```
n = q + 1  (where q is the server's prime)
g = 2      (our chosen generator)
```

2. **Why These Parameters Break DLP**:
   - When we work modulo (q + 1):
   - The multiplicative group has order q
   - This means: g^q ≡ 1 mod (q + 1)
   - All values will cycle through numbers less than q + 1

3. **The Actual Break**:
   ```
   Given: h = g^x mod n
   Where: n = q + 1, g = 2
   
   Therefore:
   h = 2^x mod (q + 1)
   ```

4. **Simple Example to Illustrate**:
   If q = 7 (for simplicity):
   - n = 8
   - Powers of 2 mod 8 cycle as:
     * 2^1 ≡ 2 mod 8
     * 2^2 ≡ 4 mod 8
     * 2^3 ≡ 0 mod 8
     * 2^4 ≡ 0 mod 8
   - We can easily find x by counting steps

### Why This Makes DLP Easy:

1. **Normal DLP vs Our Case**:
   - Normal DLP: Large prime modulus, complex group structure
   - Our case: Small modulus (q+1), simple cycling pattern

2. **Finding x Becomes Simple**:
   - Start with 1
   - Multiply by 2 repeatedly
   - Count steps until we reach h
   - That count is our x

3. **Mathematical Properties We Exploit**:
   ```
   - All values cycle quickly mod (q+1)
   - The pattern is predictable
   - No complex math needed, just counting
   ```

4. **Why g = 2 Helps**:
   - Powers of 2 are easy to compute
   - The sequence is simple to track
   - Values stay relatively small

To implement this break:

1. **Algorithm**:
```
x = 0
current = 1
while current ≠ h:
    current = (current * 2) % (q + 1)
    x += 1
return x
```

2. **Efficiency**:
   - This is much faster than traditional DLP methods
   - No need for baby-step giant-step or Pollard's rho
   - Simple multiplication and modulo operations

### Conclusion
This challenge cleverly demonstrates how the security of the discrete logarithm problem relies heavily on proper parameter selection. By allowing us to choose our own parameters, the challenge lets us transform a traditionally hard problem into a trivially solvable one.

---