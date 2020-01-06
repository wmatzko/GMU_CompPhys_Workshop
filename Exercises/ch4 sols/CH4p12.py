# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:27:14 2020

@author: William
"""
#get needed imports
import numpy as np
from random import *

#make empty list to initialize matrix
m = []

#fill list with random integers
for i in range(100):
    m.append(randint(0,9))
    
#reshape list into arbitrary matrix 
#can be anything besides 10,10, as long as the two numbers multiply to total number of elements in m
m = np.reshape(m, (10,10))

#print the matrix we've made, see if we did things right
print("The original matrix is \n {0}".format(m))
print() #readability in console

#make function to compute transpose
def transpose(m):
    '''
    Calculate transpose of matrix m
    '''
    #obtain number of rows and columns in matrix, used for bounds on loops
    row_number = m.shape[0] 
    column_number = m.shape[1]
    
    #initialize matrix to hold transpose
    mt = np.zeros(shape=(column_number, row_number))
    #loop through indices in 'horizontal' and 'vertical' directions
    for i in range(column_number):
        for j in range(row_number):
            mt[i][j] = m[j][i]#swap placement, identical to mathematical formula for transpose
    
    #print(np.transpose(m)) #transpose with numpy, library function way
    return mt

#write function to swap arbitrary rows
def row_swap(m, a, b):
    '''
    Swap the rows, a and b, of some matrix m
    '''
    #uncommenting print statements might help understand this
    
    #print(m[a]) #'grabs' one row
    #print()
    #print(m[[a,b]]) #'grabs' two rows
    #print()
    
    #simple, but not intuitive
    m[[a,b]] = m[[b,a]] #swaps rows
    
    return m
#make function to swap columns
def column_swap(m, a, b):
    '''
    Swap the columns, a and b, of a matrix m
    '''
    #transpose, then do row swaps, then transpose back
    #if you think about it, this is logically equivalent to swapping columns
    
    m = transpose(m) #swap rows and columns
    m = row_swap(m, a, b) #swap rows (they were originally columns)
    m = transpose(m) #swap rows and columns again
    
    return m

#call functions and print output, with readability in console

print("Swapping rows")
print()
print(row_swap(m, 0,9))  
print()
print("Swapping columns")
print()
print(column_swap(m, 0, 9))    

#print(transpose(m))