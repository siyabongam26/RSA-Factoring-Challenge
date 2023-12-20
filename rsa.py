#!/usr/bin/env python3

import sys
from sympy import isprime, factorint

def rsa_factorize(filename):
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        n = int(number)
        if not isprime(n):
            factors = factorint(n)
            p, q = factors.popitem()
            print(f"{n}={p}*{q}")
        else:
            print(f"{n}={n}*1")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    rsa_factorize(filename)
