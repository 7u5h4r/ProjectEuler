import sys
from math import * 
def sumsq(x):
    return pow(((1+x)*x)/2,2)
def sqsum(n):
    return (n*(n+1)*((2*n)+1))/6
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print int(sumsq(n))-sqsum(n)
