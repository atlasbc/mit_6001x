# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:45:20 2017

@author: Atlas

"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    if aList == []:
        return aList
    if type(aList[0]) == list:            
        return flatten(aList[0]) + flatten(aList[1:])    
    return aList[:1] + flatten(aList[1:])
    
    
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
alist2 = [1,2]
print(flatten(aList))
print(flatten(alist2))

