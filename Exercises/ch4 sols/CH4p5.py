# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:24:35 2020

@author: William
"""
#start with first two terms of sequence
a = 1
b = 1

#make list to hold the first two numbers
#update list with future numbers in sequence
fib = [a,b] 

#ask user what term of the Fibonacci sequence they want
n = int(input("What term of the Fibonacci sequence do you want? "))


#loop through up to n-2 (else we obtain an extra 2 terms at end of list)
for i in range(n-2):
    #calculate next term
    answer = fib[i] + fib[i+1]
    #append next term to list
    fib.append(answer)
    
#print sequence
print(fib)

#print the term the user wanted
print(fib[n-1])
