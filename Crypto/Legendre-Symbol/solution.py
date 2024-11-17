import os


def legendre_symbol(a, p):
    """
    Calculate the Legendre Symbol (a/p)
    Returns: 1 if a is a quadratic residue mod p
            -1 if a is a quadratic non-residue mod p
            0 if a is divisible by p
    """
    if a % p == 0:
        return 0
    
    # Euler's criterion
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def tonelli_shanks(n, p):
    """
    Find square root of n modulo p using Tonelli-Shanks algorithm
    Returns both square roots if they exist
    """
    # Check if n is a quadratic residue
    if legendre_symbol(n, p) != 1:
        return None
    
    # Factor out powers of 2 from p-1
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    
    # Find quadratic non-residue
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1
    
    # Initialize variables
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    
    # Main loop
    while t != 1:
        # Find least i such that t^(2^i) = 1
        i = 0
        temp = t
        while temp != 1:
            temp = (temp * temp) % p
            i += 1
            if i == m:
                return None
        
        # Update variables
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    
    # Return both square roots
    return (r, p - r)

def read_challenge_file(filename):
    """Read and parse the challenge file"""

    # Change to the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract p and ints using eval()
    exec_locals = {}
    exec(content, {}, exec_locals)
    return exec_locals['p'], exec_locals['ints']

def solve_challenge():
    # Read the challenge file
    p, numbers = read_challenge_file('output.txt')
    
    # Find the quadratic residue among the numbers
    for n in numbers:
        if legendre_symbol(n, p) == 1:
            print(f"Found quadratic residue: {n}")
            # Calculate square roots
            roots = tonelli_shanks(n, p)
            if roots:
                root1, root2 = roots
                larger_root = max(root1, root2)
                print(f"Larger square root (flag): {larger_root}")
                return larger_root
    
    return None

if __name__ == "__main__":
    try:
        flag = solve_challenge()
        if flag:
            print("\nSuccess! Found the flag.")
        else:
            print("\nFailed to find quadratic residue or its square root.")
    except Exception as e:
        print(f"Error occurred: {e}")
