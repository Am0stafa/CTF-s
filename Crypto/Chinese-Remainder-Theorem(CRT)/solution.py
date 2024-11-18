def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a: int, m: int) -> int:
    """
    Returns modular multiplicative inverse of a under modulo m
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def chinese_remainder_theorem(remainders: list[int], moduli: list[int]) -> int:
    """
    Solves the Chinese Remainder Theorem for a system of congruences
    """
    # Calculate product of all moduli
    N = 1
    for modulus in moduli:
        N *= modulus
    
    # Calculate partial products and their inverses
    result = 0
    for i in range(len(remainders)):
        Ni = N // moduli[i]
        yi = mod_inverse(Ni, moduli[i])
        result += remainders[i] * Ni * yi
    
    return result % N

# Our specific problem values
remainders = [2, 3, 5]      # x ≡ 2 (mod 5), x ≡ 3 (mod 11), x ≡ 5 (mod 17)
moduli = [5, 11, 17]        # The moduli must be coprime


solution = chinese_remainder_theorem(remainders, moduli)
print(f"Solution: {solution}")


