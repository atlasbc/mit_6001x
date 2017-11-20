# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:56:45 2017

@author: Sony
"""

def mySort(L):
    """ L, list with unique elements """
    clear = False
    i = 0
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                print(L)
                i+=1
    print(i)            
                
def newSort(L):
    """ L, list with unique elements """
    count = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            print(L)   
            count +=1
    print(count)             
            
L = [7,6,5,4,3, 2, 1]
mySort(L)
print()
L = [7,6,5,4,3, 2, 1]
newSort(L)            