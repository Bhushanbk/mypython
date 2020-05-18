class student:
    def __init__(self,aname,arno,afee):
        self.name=aname
        self.rno=arno
        self.fee=afee
    def put_details(self):
        print("name is:",self.name)
        print("rno is:",self.rno)
        print("fee is:",self.fee)
    def __del__(self):
        print("object destroyed")
obj_s1=student("john",420,42000.0)
obj_s2=student("abraham",450,47000.0)
print("obj:1 details")
obj_s1.put_details()
print("s2 on=bj details")
obj_s2.put_details()
del obj_s1
print("obj1 details")
#obj_s1.put_details()