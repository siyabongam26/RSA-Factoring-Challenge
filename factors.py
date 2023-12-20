#!/usr/bin/env python3

import sys
from sympy import factorint

def factorize(filename):
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        n = int(number)
        factors = factorint(n)
        p, q = factors.popitem()
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    factorize(filename)
