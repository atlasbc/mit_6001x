# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:08:40 2017

@author: Atlas
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """

    key_code = {}
    decoded = ''
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
        
    for letter in code:
        try:        
            decoded = decoded + (list(key_code.keys())[list(key_code.values()).index(letter)])
        except:
            decoded = decoded + letter
    return key_code, decoded    


print(cipher("abcde", "dcbaf", "dab"))
#cipher("abcd", "dcba", "dab") 
#returns (order of entries in dictionary may not be the same) 
#({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

# This took 4/20 points