# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:19:34 2020

@author: William
"""

even = []
odd = []

n = int(input("Please insert an integer > 0: "))

for i in range(n+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(even)
print() #space in console
print(odd)