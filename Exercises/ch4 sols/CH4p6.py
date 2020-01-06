# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:46:17 2020

@author: William
"""
#need to obtain e and pi, use numpy
import numpy as np

#put everything in list by hand, no shortcut I can think of
#note use j to denote complex numbers
data = [np.pi, np.e, 3, 3.0, '3.0', 3+2j, True, 2.54, [1,3,4,5], (3,5,6), [[1,2] , [3,4]]]

#loop through elements in list
for i in data:
    #for each element in the list, print the element and its data type next to it
    print(i, type(i))
    


