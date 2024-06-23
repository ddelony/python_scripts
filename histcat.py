#!/usr/bin/env python
# histcat - Print a histogram of length of lines in standard input
import fileinput
for line in fileinput.input():
	s = '=' * len(line)	
	print(s)
