#!/usr/bin/env python
# dec2bin - convert base 10 to binary 

import sys
if len(sys.argv) == 2:
    dec = int(sys.argv[1])
else:
    print("Enter decimal number:")
    dec = int(input())

bin = bin(dec)
print(bin)


