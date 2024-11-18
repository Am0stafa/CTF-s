## The Challenge

The Chinese Remainder Theorem provides a unique solution to a set of linear congruences when their moduli are coprime.

This means, that given a set of arbitrary integers `a_i`, and pairwise coprime integers `n_i`, such that the following linear congruences hold:

```
x ≡ a₁ mod n₁
x ≡ a₂ mod n₂
...
x ≡ aₖ mod nₖ
```

> **Note**: "pairwise coprime integers" means that for any two integers `n_i` and `n_j` from the set, `gcd(n_i, n_j) = 1`.

There is a unique solution `x ≡ a mod N` where `N = n₁ * n₂ * ... * nₖ`.

In cryptography, we often use the Chinese Remainder Theorem to reduce a problem of very large integers into a set of several, smaller, easier problems.

**Task**: Given the following set of linear congruences:

```
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
```

Find the integer `a` such that `x ≡ a mod 935`.

> **Hint**: Starting with the congruence with the largest modulus, use that for `x ≡ a mod p` we can write `x = a + k * p` for an arbitrary integer `k`.


---
## The Explanation:

[Your detailed explanation of the problem goes here and explain the approach to solve the problem.]

---
## The Solution:

[Your steps to solve the problem goes here step by step explaining each step.]


---