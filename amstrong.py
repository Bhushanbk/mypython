a=b=c=int(input("enter your no"))
count=0
while (a>0):
    a=a//10
    count=count+1
print(count,"is the no of digit")
rem=0
sum=0
while b:
    rem=b%10
    b=b//10
    sum=sum+rem**count
if (sum==c):
    print(sum,"is amstrong no.")
else:
    print(c,"is not an amstrong no")
