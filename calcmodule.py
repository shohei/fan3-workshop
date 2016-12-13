#!/usr/bin/env python
#-*-coding:utf-8-*_

modules = [0.25,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.125,1.25,1.375,1.5,1.75,2,2.25,2.5,2.75,3]
zs = [i+10  for i in range(101)] #10-100

for m in modules:
    ans = 78.4/m
    if ans.is_integer():
        print m,ans

#m = 0.8

