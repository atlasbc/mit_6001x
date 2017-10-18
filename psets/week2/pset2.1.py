# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:04:48 2017

@author: Atlas
Problem 1 from week 2 from mit 6.00.1x

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + 
                             (Monthly interest rate x Monthly unpaid balance)
"""

 # Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterest = annualInterestRate / 12.0

for month in range(0, 12):
    minpayment = balance * monthlyPaymentRate
    balance = balance - minpayment
    balance = balance + balance*monthlyInterest
    print(month, balance)

print("This is remaining balance", round(balance, 2))    
    



