"""Example carrier file to embed our payload in.
"""

import math

def fibV1(n):
    if n == 0 or n == 1:
        return n
    return fibV1(n - 1) + fibV1(n - 2)

def fibV2(n):
    if n == 0 or n == 1:
        return n
    return int(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n) / (2**n * math.sqrt(5)))

def main():
    result1 = fibV1(12)
    result2 = fibV2(12)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
