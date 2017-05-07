#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    th=long((n-1)/3)+1
    fv=long((n-1)/5)+1
    bo=long((n-1)/15)+1
    print (((th-1)*3)*(th))/2 + ((fv-1)*5)*(fv)/2 - ((bo-1)*15)*(bo)/2