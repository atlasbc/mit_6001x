# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:19:52 2017

@author: Atlas
"""

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    K = L[:]
    for i in K:
        if g(f(i)):
            continue
        else:
            L.remove(i)
    return max(L) if len(L) >= 1 else -1

L = [6]


print(L)
print(applyF_filterG(L, f, g))
print(L)
#Should print
#6
#[5,6]