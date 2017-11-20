# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:12:32 2017

@author: Sony
"""
import string


def build_shift_dict(shift):
    shift_dict = {}
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    
    #add lowercase
    for letter in lowercase:
        i = lowercase.find(letter)
        shift_dict[letter] = lowercase[(i + shift)%26]
        i = (i + 1) % 26    
    #add uppercase    
    for letter in uppercase:
        i = uppercase.find(letter)
        shift_dict[letter] = uppercase[(i + shift)%26]
        i = (i + 1) % 26       
    return shift_dict        
print(build_shift_dict(1))