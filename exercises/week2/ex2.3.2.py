# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:13:42 2017

@author: Atlas
Mit 2.3.2 Exercise
"""
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
