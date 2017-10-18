# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:24:54 2017

@author: Atlas
Mit example about function scope from week 2
"""
def g(x):
    def h():
        x = 'abc'
        return x
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x
x = 3
z = g(x)    

