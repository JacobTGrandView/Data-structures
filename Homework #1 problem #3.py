# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 18:31:39 2022

@author: jt108
"""

## Devise an experiment that compares the performance
## of the del operator on lists and dictionaries


import timeit

MyListTime = timeit.timeit('MyList = [1,2,3,5,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]; del(MyList[5])', number=5000)
MyDictTime = timeit.timeit('MyDict = {"Iowa": "Des Moines", "Age": 20, "School": "Grand View", "Number": "515", "Favorite Food": "Pizza", "Favorite sport": "Baseball"}; del(MyDict["School"])', number=5000)
print('List time is ', MyListTime)
print('Dictionary time is ', MyDictTime)

