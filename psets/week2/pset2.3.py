# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:23:40 2017

@author: Atlas
Problem 3 from week 2 from mit 6.00.1x

Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
          
"""

balance = 320000
annualInterestRate = 0.2
monthly_ir = annualInterestRate / 12.0
unpaid_balance = balance
fixed_rate = 0
lower_bound = unpaid_balance / 12.0
upper_bound = (unpaid_balance*(1+monthly_ir)**12)/12.0
iteration = 0


while (unpaid_balance >= 0) or (unpaid_balance <= -0.01):
    
    fixed_rate = (lower_bound + upper_bound)/2
    unpaid_balance = balance
    upper_balance = balance
    lower_balance = balance
    
    for month in range(12):
        
        unpaid_balance = unpaid_balance - fixed_rate
        unpaid_balance = unpaid_balance + unpaid_balance*monthly_ir
        
        lower_balance = lower_balance - lower_bound
        lower_balance = lower_balance + lower_balance*monthly_ir
        
        upper_balance = upper_balance - upper_bound
        upper_balance = upper_balance + upper_balance*monthly_ir

    if (abs(lower_balance) < abs(upper_balance)):
        upper_bound = fixed_rate
    else:
        lower_bound = fixed_rate                
    iteration += 1  
    
print("Lowest payment:", round(fixed_rate,2))
print("Balance:", unpaid_balance)
print("Number of iterations are:", iteration)
