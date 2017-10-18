# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:53:53 2017

@author: Atlas
Mit 6.00.1x Function scope example
"""
def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f(x)