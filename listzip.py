# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:13:48 2019

@author: hp
"""

name = ["manjeet","nikhil","bhushan","ronaldo"]
roll_no=[4,3,2,1]
marks=[40,50,60,70]
mapped=zip(name,roll_no,marks)
mapped=list(mapped)
print("the zip result is:",end="")
print(mapped)