f=open("file.txt",'w')
f.write("helo world \n")
f.write("hi how are you \n")
f.write("whats sup\n")
f=open("file.txt",'r')
content=f.readlines()
for line in content:
   print(line) 

