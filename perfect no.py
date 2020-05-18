a=7
sum=0
for j in range(1,a):
    if a%j==0:
        sum=sum+j
if (sum==a):
    print("perfect no",sum)
else:
    print("not a perfect",a)    