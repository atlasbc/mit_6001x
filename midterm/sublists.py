# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:13:57 2017

@author: Atlas

Problem Definition:
Write a function called getSublists, which takes as parameters a list of 
integers named L and an integer named n.

assume L is not empty
assume 0 < n <= len(L)
This function returns a list of all possible sublists in L of length n without 
skipping elements in L. The sublists in the returned list should be ordered in 
the way they appear in L, with those sublists starting from a smaller index 
being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function 
should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], 
[3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return 
the list [[1, 1], [1, 1], [1, 1], [1, 4]]
"""

def getSublists(L, n):
    '''
    input:
        L: a list
        n: an integer
        L must not be empty
        n cannot be bigger than list's length
    output: n sublist part of the list in a list    
    '''
    output = []
    count = 0    
    sublist = []
    while count <= (len(L) - n):
        sub_count = 1
        for element in L[(count):len(L)]:     
            sublist.append(element)
            if sub_count % n == 0:
                output.append(sublist)
                sublist = []
                break
            sub_count += 1
        count += 1
    return output
          
        
    
    
#print(getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4))   
#print() 
#print(getSublists([1, 1, 1, 1, 4], 2))
print(getSublists(range(-1, -51, -1), 5))