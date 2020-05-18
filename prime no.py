# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:04:00 2019

@author: hp
"""

a=12345
rem=0
sum=0
for i in range(a):
    rem=a%10
    a=a//10
    sum+=rem
print("sum is " ,sum)