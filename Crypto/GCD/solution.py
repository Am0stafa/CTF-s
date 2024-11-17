# Here is an efficient implementation of Euclid's Algorithm
def gcd(a: int, b: int) -> int:
    # Handle negatives and zeros
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    
    # Optimization 1: Handle common cases immediately
    if a == b: return a
    if a == 1 or b == 1: return 1
    
    # Optimization 2: Quick check for coprime numbers
    if a % 2 == 1 and b % 2 == 1:
        # If both numbers are odd and one divides evenly into the other
        # they might be coprime - do a quick check
        if a % b == 0: return b
        if b % a == 0: return a
    
    # Optimization 3: Enhanced binary GCD
    # Remove common factors of 2
    shift = 0
    while not ((a | b) & 1):  # Both even
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove remaining factors of 2 from a
    while not (a & 1):
        a >>= 1
    
    # Main loop - optimized binary version
    while b:
        # Remove factors of 2 from b (a is already odd)
        while not (b & 1):
            b >>= 1
            
        # Ensure a >= b
        if a < b:
            a, b = b, a
            
        # Reduce larger number
        a = a - b  # Remove unconditional shift, just subtract
        
    # Restore common factors of 2
    return a << shift


# Test the implementation
a = 12
b = 8
print(gcd(a, b))
