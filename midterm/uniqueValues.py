# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:00:07 2017

@author: Atlas
problem definition:
    
Write a Python function that returns a list of keys in aDict that map to 
integer values that are unique (i.e. values appear exactly once in aDict). 
The list of keys you return should be sorted in increasing order. 
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.    
"""
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    output_key = []
    value_list = []
    # Your code here
    for key in aDict:
        if aDict[key] not in value_list and (list(aDict.values()).count(aDict[key]) <= 1):
            output_key.append(key)
    output_key.sort()
    
    return output_key        

#print(uniqueValues({1: 1, 2: 1, 3: 1})) #returns 0
#print(uniqueValues({2: 0, 3: 3, 6: 1})) #returns [2, 3, 6]
print(uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})) 
#returns [0, 1, 2, 3, 5, 6, 7, 9, 10]
print(uniqueValues({0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0}))
#returns [3, 7, 9]