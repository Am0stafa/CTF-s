def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Returns (gcd, u, v) such that a*u + b*v = gcd(a,b)
    Using binary optimization for efficiency
    """
    # Handle special cases
    if a == 0: return b, 0, 1
    if b == 0: return a, 1, 0
    
    # Initialize coefficients
    u, v, u1, v1 = 1, 0, 0, 1
    
    # Store original inputs for coefficient calculations
    orig_a, orig_b = a, b
    
    # Extract common powers of 2
    shift = 0
    while not ((a | b) & 1):  # While both a and b are even
        a >>= 1
        b >>= 1
        shift += 1
    
    # Store initial a for later
    initial_a = a
    
    while not (a & 1):
        a >>= 1
        if not ((u | u1) & 1):  # If both u and u1 are even
            u >>= 1
            u1 >>= 1
        else:
            u = (u + orig_b) >> 1
            u1 = (u1 - orig_a) >> 1
    
    while b != 0:
        while not (b & 1):
            b >>= 1
            if not ((v | v1) & 1):
                v >>= 1
                v1 >>= 1
            else:
                v = (v + orig_b) >> 1
                v1 = (v1 - orig_a) >> 1
        
        if a > b:
            a, b = b, a
            u, v = v, u
            u1, v1 = v1, u1
        
        b -= a
        v -= u
        v1 -= u1
    
    # Restore common factor of 2
    gcd = a << shift
    
    # Ensure coefficients satisfy Bézout's identity
    return gcd, u, v

# Solve for the given prime numbers
p, q = 26513, 32321
gcd, u, v = extended_gcd(p, q)

# Verify the result
assert p*u + q*v == gcd, "Failed to find valid coefficients"

# Print the lower value as required
result = min(u, v)
print(f"The flag is: {result}")
