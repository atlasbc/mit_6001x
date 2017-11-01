# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:32:55 2017

@author: Atlas
"""
def genPrimes():
    next = 2
    primes = []      
    while True:
        is_prime = True
        for i in range(len(primes)):
            if next % primes[i] == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(next)            
            yield next            
        next += 1
prime = genPrimes()