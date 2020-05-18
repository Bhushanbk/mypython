
    def __init__(self,num=0):
        self.number=num
    def __iter__(self):
        self.x=1
        return self
    def __next__(self):
        if self.x <=self.number:
            own_iter=self.x
            self.x +=1
            return own_iter
        else:
            raise StopIteration
for x in owniterator(10):
    print("num is",x)            
            
            
            
            