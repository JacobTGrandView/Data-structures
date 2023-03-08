# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:07:26 2022

@author: jt108
"""

import random
import timeit



def binary_search_rec(a_list, item):
	    if len(a_list) == 0:
	        return False
	    midpoint = len(a_list) // 2
	    if a_list[midpoint] == item:
	        return True
	    elif item < a_list[midpoint]:
	        return binary_search_rec(a_list[:midpoint], item)
	    else:
	        return binary_search_rec(a_list[midpoint + 1 :], item)
	

test_list = []
for i in range(25):
    RandNum = random.randint(0,1000)
    test_list.append(RandNum)
	
test_list.sort()
print(test_list)


print("Recursive binary search time is ", timeit.timeit(str(test_list)))



''' ### check if number is in list
print(binary_search_rec(test_list, 3))
print(binary_search_rec(test_list, 13))
'''




def binary_search(a_list, item):
	    first = 0
	    last = len(a_list) - 1
	
	    while first <= last:
	        midpoint = (first + last) // 2
	        if a_list[midpoint] == item:
	            return True
	        elif item < a_list[midpoint]:
	            last = midpoint - 1
	        else:
	            first = midpoint + 1
	
	    return False
	
	
test_list1 = []
for i in range(25):
    RandNum = random.randint(0,1000)
    test_list1.append(RandNum)
	
test_list1.sort()
print(test_list1)


print("Iterative binary search time is ", timeit.timeit(str(test_list1)))




''' ### check if number in list
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
'''

