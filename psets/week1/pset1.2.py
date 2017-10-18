# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:09:38 2017

@author: Atlas

This is pset 1.2 from mit 6.00.1x
"""

# Paste your code into this box 
s = 'doboowboobheobobb'
found = 0
count = 0
current = 0
while found != -1:
    found = s.find("bob", current)
    if found == -1:
        break
    if found != current or found == 0:
        count += 1
    current = found + 1    
print("Number of times bob occers is:", count)      