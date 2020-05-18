import functools
import operator
lis =(1,3,5,6,2)
print("the sum of the list elements is:",end=" ")
print(functools.reduce(operator.add,lis))
print("the product of list ele is",end=" ")
print(functools.reduce(operator.mul,lis))
print("the concated product is;",end=" ")
print(functools.reduce(operator.add,["geek","for","geeks"]))
