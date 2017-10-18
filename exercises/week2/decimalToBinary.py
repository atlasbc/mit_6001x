# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:34:12 2017

@author: Atlas
Converts decimal to Binary
An MIT example from week2
"""

num = int(input())
decimal = num
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result

print("Decimal number: " + str(decimal) + " is equal to binary " + result)            
        
