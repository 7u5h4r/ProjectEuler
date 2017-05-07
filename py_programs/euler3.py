#!/bin/python
import sys
from math import *
def Euler3(n):
    x=int(sqrt(n))
    for i in range(2,x+1):
        while n % i == 0:
            n //= i
            if n == 1 or n == i:
                return i
    return n
t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print Euler3(n)