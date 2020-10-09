# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:46:05 2020

@author: AKASH
"""
print("For list1")
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3] 
for number in list1:
    if number<0:
        continue
    print(number,"\t")
print("\n")    
print("For list2")    
for number in list2:
    if number<0:
        continue
    print(number)