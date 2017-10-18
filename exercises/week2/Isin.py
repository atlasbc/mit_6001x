# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:46:51 2017

@author: Sony
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = int(len(aStr)/2)
    if aStr and char == aStr[middle]:
        return True
    elif len(aStr) <= 1:
        return False        
    else:
        if char > aStr[middle]:
            return isIn(char, aStr[middle+1:])
        elif char < aStr[middle]:
            return isIn(char, aStr[:middle])
        else:
            return False
        
print(isIn('h', 'qu'))        