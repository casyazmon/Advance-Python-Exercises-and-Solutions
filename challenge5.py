#!/usr/bin/env/python
# program that calculate and print value according to the formula Q= Square root of [(2*C*D)/H]

# C = 50, H = 30
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

c=50
h=30

value = [] # empty list to store value

items = [x for x in raw_input("Enter values of D:\n").split(',')] # same as writting
# for x in raw_input():
#	x.split(',')
for d in items:
	value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
	
print ','.join(value)
print "_____________________________________________"

