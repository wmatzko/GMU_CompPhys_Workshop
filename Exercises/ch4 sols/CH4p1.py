# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:58:50 2020

@author: William
"""
#need to import e and pi, use numpy for this
import numpy as np 
#assign numpy values to variables
e = np.e
pi = np.pi 
#add the two numbers
add = e + pi

#print the result to 4 decimal places, with some context
print("The value of e + pi is {0:.4f}".format(add))
