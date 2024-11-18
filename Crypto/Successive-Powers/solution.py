def find_p_and_x():
    nums = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
    
    # Try all possible three-digit primes for p from 100 to 999
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Generate three-digit primes from 100 to 999
    primes = [p for p in range(100, 1000) if is_prime(p)]
    
    for p in primes:
        # For each prime p, try to find x
        # For consecutive pairs (a,b) we should have: b ≡ a*x (mod p)
        potential_x = set()
        
        # From first pair, find possible x values
        a, b = nums[0], nums[1]
        # Find x where: b ≡ a*x (mod p)
        for x in range(p):
            if (a * x) % p == b:
                potential_x.add(x)
        
        # Test each potential x against all pairs
        for x in potential_x:
            valid = True
            # Verify all consecutive pairs
            for i in range(len(nums)-1):
                if (nums[i] * x) % p != nums[i+1]:
                    valid = False
                    break
            
            if valid:
                return p, x
    
    return None, None


if __name__ == "__main__":
    p, x = find_p_and_x()
    if p and x:
        print(f"Found solution: p = {p}, x = {x}")

        result = []
        val = x
        for _ in range(12):
            result.append(val % p)
            val = (val * x) % p
        print("Verification:", result)
    else:
        print("No solution found")
