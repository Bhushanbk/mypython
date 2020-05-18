def  calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
num=5
fact=calc_factorial(num)
print("the factorial of",num,"is",fact)        