#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    a=2
    b=1
    su=2
    suu=0
    n = int(raw_input().strip())
    while(su<n):
        a=su
        su+=b        
        b=a
        if(b%2==0):
            suu+=b
        
    print suu