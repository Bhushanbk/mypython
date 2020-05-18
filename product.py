a=523
rem=0
sum=1
while a:
    rem=a%10
    a=a//10
    sum=sum*rem
print("sum is " ,sum)