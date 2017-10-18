# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:41:16 2017

@author: Atlas
Mit 2.week exercise guess my number

Problem Definition:
    In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!

"""
low = 0
high = 100
secret_number = int((low+high)/2)
print("Please think of a number between 0 and 100!")
answer = None
while answer != 'c':
    print("Is your secret number", secret_number)
    print("Enter 'h' to indicate the guess is too high", end='')
    print("Enter 'l' to indicate the guess is too low.", end='')
    print("Enter 'c' to indicate I guessed correctly.", end=' ')
    answer = input()  
    if answer == 'l':
        low = secret_number
    elif answer == 'h':
        high = secret_number
    elif answer == 'c':
        print("Game over. Your secret number was:", secret_number)
    else:        
        print("Sorry, I did not understand your input.")
    secret_number = int((low+high)/2)
    
