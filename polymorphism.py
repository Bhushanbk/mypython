class poly:
    def add1(self,a,b):
        return a+b
    def add1(self,a,b,c):
        return a+b+c
    def add1(self,a,b,c,d):
        return a+b+c+d
fun_ovr=poly()
#two_sum=fun_ovr.add1(1,3)
#three_sum=fun_ovr.add1(3,4,5)
four_sum=fun_ovr.add1(3,4,5,6)
#print("two_sum",two_sum)
#print("three_sum",three_sum)
print("str_sum is:",four_sum) 