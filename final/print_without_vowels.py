# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:28:34 2017

@author: Atlas
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = 'aeiouAEIOU'
    stripped = ''
    for i in s:
        if i in vowels:
            stripped = stripped + ''
        else:
            stripped = stripped + i
    print(stripped)        
    
print_without_vowels("This is great!")