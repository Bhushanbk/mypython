# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:53:10 2019

@author: hp
"""

num=int(input("enter number:"))
temp=num
rev=0
while num:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
if rev==temp:
    print("equal")
else:
    print("not equal")                 