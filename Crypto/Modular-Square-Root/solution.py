import os
from sympy import *

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

p, a = read_challenge_file('output.txt')
print(sqrt_mod(a, p))