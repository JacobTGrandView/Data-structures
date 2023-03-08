# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:39:28 2022

@author: jt108
"""

def factorial(n):
    if(n == 1) or (n == 0):
        return 1
    else:
        return(n * factorial(n-1))

number = 6
print(factorial(number))