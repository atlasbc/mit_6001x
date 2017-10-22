# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:22:02 2017

@author: Atlas
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    tupplelist=[]
    print("This is the length of tuple", len(aTup))
    for i in range(len(aTup)):
        print(aTup[i])
        if i % 2 == 0:
            print(i)
            tupplelist.append(aTup[i])
    return tuple(tupplelist)

print(oddTuples((8,)))