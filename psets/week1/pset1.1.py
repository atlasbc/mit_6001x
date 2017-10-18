# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:33:10 2017

@author: Atlas
This is pset 1.1 from mit 6.00.1x
"""
s = 'azcbobobegghakl'
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
        count += 1
print("Number of vovels: " + str(count)) 