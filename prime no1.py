a=7
for i in range(2,a):
    if a%i==0:
        print (a,"is divisible by",i,"not a prime")
        break
else:
    print(a,"is a prime no")        