# -*- coding: utf-8 -*-
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exp = 0
    suc_exp = 1
    closest = 0
    while base**exp <= num:
        if abs((base**exp - num)) <= abs((base**suc_exp - num)):
            closest = exp
        else:
            closest = suc_exp
        exp += 1
        suc_exp += 1
    return closest
    

#print(closest_power(3,12)) #returns 2
#print(closest_power(4,12)) #returns 2
#print(closest_power(4,1)) #returns 0    
print(closest_power(2, 192.0)) #returns 7
print(closest_power(5, 375.0)) #returns 3
print(closest_power(20, 210.0)) #returns 1
print(closest_power(10, 550.0)) #returns 2
