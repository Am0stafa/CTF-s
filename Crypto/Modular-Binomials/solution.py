from math import gcd
from Crypto.Util.number import GCD

def solve_modular_binomials(N, e1, e2, c1, c2):
    # Calculate p^(e1e2) mod N
    # This comes from the simplified binomial expansion
    p_power = pow(2, e1 * e2, N)  # This represents (2p)^(e1e2)
    
    # Calculate GCD to extract p
    p = GCD(p_power, N)
    
    # Calculate q
    q = N // p
    
    return p, q

# Use the values from data.txt
p, q = solve_modular_binomials(N, e1, e2, c1, c2)
print(f"p = {p}")
print(f"q = {q}")
print(f"Verification: p * q == N: {p * q == N}")
