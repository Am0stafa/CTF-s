def find_quadratic_residue(n, p):
    """
    Check if n is a quadratic residue modulo p and return its square root if it exists
    """
    # Try values from 1 to (p-1)/2
    for x in range(1, (p + 1) // 2 + 1):
        if (x * x) % p == n:
            # Found a square root! Return both positive and negative roots
            return True, (x, p - x)
    return False, None

def solve_challenge():
    p = 29
    numbers = [14, 6, 11]
    
    # Check each number
    for n in numbers:
        is_residue, roots = find_quadratic_residue(n, p)
        if is_residue:
            print(f"{n} is a quadratic residue mod {p}")
            smaller_root = min(roots)
            print(f"Square roots are {roots}, smaller root is {smaller_root}")
            return smaller_root
        else:
            print(f"{n} is NOT a quadratic residue mod {p}")
    
    return None

if __name__ == "__main__":
    flag = solve_challenge()
    print(f"\nFlag: {flag}")
