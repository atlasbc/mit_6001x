# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:40:46 2017

@author: Atlas

This is pset 1.3 from mit 6.00.1x

Problem Definition:
    Assume s is a string of lower case characters.

    Write a program that prints the longest substring of s in which the letters
    occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
    then your program should print

    Longest substring in alphabetical order is: beggh
    
    In the case of ties, print the first substring. 
    For example, if s = 'abcbcd', then your program should print

    Longest substring in alphabetical order is: abc
"""
s = 'mkqxeufvcobhowwwxllxk'
i = 0 #first location
j = 1 #succeeding location
length = 0 #temporary substring's length
t_length = 0 #longest substring's length
start = 0   #temporary substring's start position
end = 0     #temporary substring's end position
t_start = 0 #longest substring's start position
t_end = 0   #longest substring's end position

while end < len(s):
    
    if j >= len(s):
        break
    
    if length == 0:
        start = i
        
    if ord(s[j]) >= ord(s[i]):
        length += 1
        end = j
        i += 1
        j += 1
        
        if j > length:
            if length > t_length:
                t_start = start
                t_end = end
    else:
        if length > t_length:
            t_length = length
            t_start = start
            t_end = end
        length = 0
        i += 1
        j += 1

print("Longest substring in alphabetical order is:", s[t_start:t_end+1])        
        
         
        
        
    
          
