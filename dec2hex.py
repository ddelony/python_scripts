#!/usr/bin/env python
# dec2hex - convert base 10 to base 16

import sys
if len(sys.argv) == 2:
	dec = int(sys.argv[1])
else:
	print("Enter decimal number:")
	dec = int(input())

hex = hex(dec)
print(hex)


