import requests
import math
from bs4 import BeautifulSoup

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a
  
def extendedGCD(a,b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, y, x = extendedGCD(b%a, a)
    return (gcd, x - (b//a) * y, y)
    
def coprime(a):
    for i in range(2, a):
        if math.gcd(a, i) == 1:
            return i
    return -1
    
def multiplicativeInverse(a, m):
    g, x, y = extendedGCD(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
    
# long division
def longDivision(a, b):
    q = a // b
    r = a % b
    return q, r

# long division with polynomials
def longDivisionPoly(a, b):
    q = []
    r = a
    while len(r) >= len(b):
        q.append(r[0] / b[0])
        r = [x - y * q[-1] for x, y in zip(r, b)]
        r = r[1:]
    return q, r





def main():
    # print(gcd(24, 15))
    # print(extendedGCD(101, 103))
    # print(coprime(10))
    # print(multiplicativeInverse(89,100))

    # print(phi(7))
    # print(longDivision(10, 3))
    # print(longDivisionPoly([1, 2, 3, 4], [1, 2, 3]))

   
main()