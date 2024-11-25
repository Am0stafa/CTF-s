from math import gcd
from Crypto.Util.number import long_to_bytes

def read_data(filename="data.txt"):
    """Read the challenge data from file"""
    with open(filename, 'r') as f:
        data = f.read()
        # Extract values using eval() for each line
        N = int(data.split('N = ')[1].split('\n')[0])
        e1 = int(data.split('e1 = ')[1].split('\n')[0])
        e2 = int(data.split('e2 = ')[1].split('\n')[0])
        c1 = int(data.split('c1 = ')[1].split('\n')[0])
        c2 = int(data.split('c2 = ')[1].split('\n')[0])
    return N, e1, e2, c1, c2

def solve_modular_binomials(N, e1, e2, c1, c2):
    """
    Solve the modular binomial equations to find primes p and q
    Using the method:
    g₁ = c₁^e₂ ≡ (2p + 3q)^(e₁e₂) mod N
    g₂ = c₂^e₁ ≡ (5p + 7q)^(e₁e₂) mod N
    """
    # Calculate g1 and g2
    g1 = pow(c1, e2, N)  # g1 = c1^e2 mod N
    g2 = pow(c2, e1, N)  # g2 = c2^e1 mod N
    
    # Calculate powers of 2 and 5
    power_2 = pow(2, e1 * e2, N)
    power_5 = pow(5, e1 * e2, N)
    
    # Calculate D = 5^(e1e2)g1 - 2^(e1e2)g2
    D = (power_5 * g1 - power_2 * g2) % N
    
    # Find q using GCD
    q = gcd(D, N)
    
    # Calculate p
    p = N // q
    
    return p, q

def verify_solution(p, q, N, e1, e2, c1, c2):
    """Verify that the found solution is correct"""
    # Check if p * q = N
    if p * q != N:
        return False
    
    # Check first equation: c1 = (2p + 3q)^e1 mod N
    if pow(2*p + 3*q, e1, N) != c1:
        return False
    
    # Check second equation: c2 = (5p + 7q)^e2 mod N
    if pow(5*p + 7*q, e2, N) != c2:
        return False
    
    return True

def main():
    # Read the challenge data
    print("[+] Reading challenge data...")
    N, e1, e2, c1, c2 = read_data()
    
    print("[+] Solving modular binomials...")
    p, q = solve_modular_binomials(N, e1, e2, c1, c2)
    
    print("[+] Verifying solution...")
    if verify_solution(p, q, N, e1, e2, c1, c2):
        print("[+] Solution verified!")
        print(f"\np = {p}")
        print(f"q = {q}")
        
        # Try to decode potential flag from p or q
        try:
            flag_from_p = long_to_bytes(p)
            print(f"\nPotential flag from p: {flag_from_p.decode()}")
        except:
            pass
            
        try:
            flag_from_q = long_to_bytes(q)
            print(f"Potential flag from q: {flag_from_q.decode()}")
        except:
            pass

if __name__ == "__main__":
    main()
