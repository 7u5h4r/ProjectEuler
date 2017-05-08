import sys
from math import *
def prime(x):
    return all(x%i for i in xrange(2,int(x/2)+1))
def m(y):
    if(prime(i)):
        for j in xrange(1,n+1):
            p=int(pow(i,j))
            if(p>n):
                return pow(i,(j-1))
    return 1
t = int(raw_input().strip())
for a0 in xrange(t):
    a=[]
    b=[]
    an=1
    n = int(raw_input().strip())
    for i in xrange(2,n+1):
        an=an*m(i)
    print int(an)