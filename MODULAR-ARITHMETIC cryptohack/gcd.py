def gcd(a,b):
  while b:
    a,b = b, a%b
  return a
  
# extended euclidean algorithm

def extendedGCD(a,b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = extendedGCD(b%a, a)
    return (g, x - (b//a) * y, y)
    
print(extendedGCD(26513,32321))