my_list=[1,2,4,5,6,78,9,60]
new_list=list(filter(lambda x: (x%2==0),my_list))
new_list1=list(map(lambda x: (x%2==0),my_list))
print(new_list,new_list1)