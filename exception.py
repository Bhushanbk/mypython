# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:54:37 2019

@author: hp
"""
a=int(input("enter the no"))
b=int(input("enter the no"))
try:
    res=a/b
    print("result",res)
except ZeroDivisionError:
    print("sorry")    