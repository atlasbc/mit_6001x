# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:52:13 2017

@author: Atlas
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    numbers = set(L)
    numbers = sorted(numbers, reverse=True)
    for number in numbers:
        if (L.count(number) % 2) == 1:
            return number
    return None    

    


print(largest_odd_times([2,2,4,4]))
print
print(largest_odd_times([3,9,5,3,5,3]))

#largest_odd_times([2,2,4,4]) returns None
#largest_odd_times([3,9,5,3,5,3]) returns 9    