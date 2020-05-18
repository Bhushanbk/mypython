# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:04:32 2019

@author: hp
"""

try:
    value1=int(input("enter the no"))
    value2=int(input("enter the no"))
    result=value1/value2
    print("result",result)
except ZeroDivisionError:
    print("zero error")
except ValueError:
    print("val error")
except IndentationError:        
    print("indentation error")
finally:
    print("final")    