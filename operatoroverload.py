class operatorovr():
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __str__(self):
        return"({0}),{1})".format(self.a,self.b)
    def __sub__(self,other):
        a=self.a - other.a
        b=self.b - other.b
        return operatorovr(a,b)
obj1=operatorovr(2,3)
obj2=operatorovr(2,2)
obj=operatorovr(2,2)
print("addtion of twoo obj is",obj1 -obj2-obj)    