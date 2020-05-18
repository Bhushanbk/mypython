def add(number,callback):
    results=[]
    for i in number:
        results.append(callback(i))
    return results
def add2(number):
    return number + 2
def mul2(number):
    return number * 2 
print(add([1,2,3,4],add2))
print(add([1,2,3,4],mul2))