# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:31:11 2019

@author: hp
"""

class student:
    database="student"
    def get_details(self,aname,arno,afee):
        self.name=aname
        self.rno=arno
        self.fee=afee
    def put_details(self):
        print("name is:",self.name)
        print("rno is:",self.rno)
        print("fee is:",self.fee)
        print("database is:",self.database)
s1=student()
s2=student()
print("object:1st created object details")
s1.get_details("john",420,42000.0)
s1.put_details()
print("database is",student.database)
print("object:2nd obj detals")
s2.get_details("abraham",450,47000.0)
s2.put_details()
print(">>>>>>>>>>>>>>>after student database>>>>")
s1.database="john"
print("obj:1 details")
s1.put_details()
print("s2 on=bj details")
s2.put_details()

        