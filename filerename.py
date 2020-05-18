import os
os.rename("C:\\Users\\hp\\Desktop\\sample.txt","C:\\Users\\hp\\Desktop\\new_file.txt")
f=open("C:\\Users\\hp\\Desktop\\new_file.txt")
data=f.read()
print(data)