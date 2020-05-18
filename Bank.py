# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:32:49 2019

@author: hp
"""
from random import randrange
class Mybank:
    def account_details(self):
        l1=[]
        self.name=input("enter your name")
        self.phone=input("enter your phone_no")
        self.pin=input("enter your pin")
        self.ac_no=randrange(10000000,999999999)
        print(self.ac_no)
        l1.append(self.name,self.phone,self.pin,self.ac_no)
        l2=[]
        l2.insert(l1)
        print(l2)
        
        
m=Mybank()
m.account_details()        
    
        