# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:57:41 2020

@author: William
"""
#not allowed to use library functions, but will show you anyways
import numpy as np

#make arbitrary vectors
a=[-1,2,3]
b = [4,5,6]

#make function to compute cross product
def cross_product(x,y):
    '''
    Calculate cross product of two vectors x,y
    x and y should be given as lists
    '''
    #cross product is vector, made by evaluating determinate of a matrix
    #refer to page 7 of lecture notes for the determinate you need to evaluate
    #don't know easy way to do determinate without library functions
    #use a 'brute force' method by just explicitly accessing components of matrix
    #[1,1,1] are unit vectors
    m = [[1,1,1], x, y] 
    print(m)
    det = m[0][0]*(m[1][1] * m[2][2] - m[1][2]*m[2][1])\
        - m[0][1]*(m[1][0] * m[2][2] - m[1][2] * m[2][0])\
        + m[0][2]*(m[1][0] * m[2][1] - m[1][1] * m[2][0])
        
    #the \ is a line break to break up a long line of code. Helps for readability
    #cannot put ANYTHING after line break, including comments
    
    #above explicitly uses matrix, but somewhat inefficient
    #you can notice that all m[0] are 1, and can access elements of x and y directly...
    #as in, you don't need to put them in a matrix
    #I encourage you to do this on your own and check that you get the same answer
    #this is good indexing practice!
    
    #print(det, np.linalg.det(m)) #compute determinate using our method, and numpy's method
    
    return det

#call function
cross_product(a,b)