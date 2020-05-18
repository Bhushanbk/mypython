def sum(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    return add,sub,mul
a=int(input("enter your no."))
b=int(input("enter your no."))
a,su,mu=sum(a,b)
print(a,su,mu)