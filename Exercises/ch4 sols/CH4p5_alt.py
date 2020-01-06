# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:40:17 2020

@author: 
"""
#Alternative, cleaner, solution
#written by <don't know name, sorry. please tell me and I'll put it here>


fibos = []
def fib(i):
    m, n = 1, 0
    for i in range(i):
        m, n = n, m+n
        fibos.append(n)
    return n

num = int(input("The number: "))
print(fib(num))
print(fibos)