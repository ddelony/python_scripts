#!/usr/bin/env python
# prime - Find prime factors
import sys

def prime(n):
    factors = []
    divisor = 2 # Start at smallest prime

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        print("Number to be factored required:")
        number = int(input())
    
    print(prime(number))
    
    
