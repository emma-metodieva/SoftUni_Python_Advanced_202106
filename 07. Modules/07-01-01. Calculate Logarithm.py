# 07-01. Modules - Lab
# 01. Calculate Logarithm

from math import log

number = int(input())
base = input()

if base == 'natural':
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(base)):.2f}")
