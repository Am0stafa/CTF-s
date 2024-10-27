# Here is an efficient implementation of Euclid's Algorithm
def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    
    # Optimization 1: Handle common cases immediately
    if a == 0: return b
    if b == 0: return a
    if a == b: return a
    
    # Optimization 2: Use binary operations for powers of 2
    # Remove common factors of 2
    shift = 0
    while not ((a | b) & 1):  # Both even
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove remaining factors of 2 from a
    while not (a & 1):
        a >>= 1
        
    # Remove remaining factors of 2 from b
    while not (b & 1):
        b >>= 1
    
    # Main loop - optimized iterative version using modulo
    while b:
        if a > b:
            a, b = b, a
        b = b % a
    
    # Restore common factors of 2
    return a << shift


# Test the implementation
result = gcd(66528, 52920)  # Should output 24
print(result)
