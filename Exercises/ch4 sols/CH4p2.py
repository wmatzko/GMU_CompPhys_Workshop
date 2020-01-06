# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:03:05 2020

@author: William
"""
#prompt user to input an integer
n = input("Please input an integer > 0: ")

#above input is string, must convert to integer
n = int(n)

#make variable to 'hold' value of sum
hold_sum = 0

#want to loop over n = 1, n = 2, n = 3, ...
for i in range(0,n+1):
    #add each number in loop to hold_sum
    hold_sum = hold_sum + i
    
#print sum
print(hold_sum)

#alternative formula, more direct 
answer = n*(n+1)/2

print(answer)
