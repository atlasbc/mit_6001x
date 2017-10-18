# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:43:41 2017

@author: Atlas
Hanoi tower example from mit 6.00.1x from week 2
"""

def printMove(fr, to):
    print('move from' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))        
