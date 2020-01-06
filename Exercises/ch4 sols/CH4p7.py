# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:35:50 2020

@author: William
"""
import numpy as np

#make arbitrary test vectors (can be any dimension)
a = (13,-3,1)
b = (-8,4,3)

#make a function to find magnitude of a vector
def magnitude(x):
    #this is a 'doc string' and tells us what the function does. Optional to include
    '''
    Calculate magnitude of a vector x
    '''
    mag = 0
    for i in x:
        #sum squared elements in vector
        mag += i**2 #shorthand notation for mag = mag + i
    mag = np.sqrt(mag) #take square root of sum to obtain magnitude
    
    return mag #return the magnitude of the vector

#write function to calculate dot product of two vectors
def dot_product(x,y):
    '''
    Compute dot product of two vectors
    '''
    
    dot_product = 0 #initialize variable to hold sum
    
    # loop through elements in both vectors
    #len(a) returns number of elements in list
    #a and b must be same length, else dot product not defined
    
    for i in range(len(a)):
        dot_product += a[i]*b[i]
    
    return dot_product

def angle(x,y):
    '''
    Calculate the angle between two vectors
    Uses the above two functions
    '''
    #use formula derived in class
    arg = dot_product(x,y)/(magnitude(x) * magnitude(y))
    #take arccos of the argument to obtain the angle, theta, between the vectors
    theta = np.arccos(arg) #calculate theta, in RADIANS
    
    return theta 

print(angle(a,b))
    
    