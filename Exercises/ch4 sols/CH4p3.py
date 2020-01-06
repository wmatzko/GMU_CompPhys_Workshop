# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:10:18 2020

@author: William
"""
#just want randint, but might as well import everything
from random import *

#make empty list to hold the integers we make
m = []

n = 10 #set number of integers we want in list
for i in range(0,n):
    #generate random integer between 0 and 20 inclusive (could use any bounds here)
    rand = randint(0,20)
    
    #append the integer to the list
    m.append(rand)
    

#let's see what random numbers we've put in our list
#this tells us if we did it right
print(m)

#now, loop through elements of list
for i in m:
    #want to check IF something is even -> if statement
    if i%2==0:
        #print to console
        print(i, "even")
    else:
        print(i, "odd")
        
