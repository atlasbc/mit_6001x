# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:50:51 2017

@author: Atlas
Problem 2 from week 2 from Mit 6.00.1x

This program finds lowest payment within 12 month for paying credit balance
with heuristic approach

"""
balance = 4773
annualInterestRate = 0.2
monthly_ir = annualInterestRate / 12.0
unpaid_balance = balance
fixed_rate = 0

while unpaid_balance > 0:
    fixed_rate += 10
    unpaid_balance = balance
    
    for month in range(12):
        unpaid_balance = unpaid_balance - fixed_rate
        unpaid_balance = unpaid_balance + unpaid_balance*monthly_ir
print("Lowest payment:", fixed_rate)
print("Balance:", unpaid_balance)        