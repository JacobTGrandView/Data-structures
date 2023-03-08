# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:07:39 2022

@author: jt108
"""

import random


### Finding the kth smallest number in a list ###
'''
MyList = []
for i in range(50):
    RandNum = random.randint(0,1000)
    MyList.append(RandNum)
	
MyList.sort()
print("Sorted list: ", MyList)

k = int(input("Enter the value for which you want to find the kth smallest number: "))
if(k>=0 and k<50):
    print("The value of", k, "is :", MyList[k])
else:
    print("That value is not within the list range")
'''
    
    
### Printing middle item in a list ###
    
MyList1 = []
for i in range(50):
    RandNum = random.randint(0,1000)
    MyList1.append(RandNum)
    
MyList1.sort()
print("Sorted list: ", MyList1)
print("Middle item is: ", MyList1[int(len(MyList1)/2)])




    
