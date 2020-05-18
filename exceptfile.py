import os
filename=input("enter the filename")
f=open(filename,"w+")
f.write("helo \nhi\nwelcome")
try:
    f=open(filename,"r")
    for line in f:
        print(line,ends="")
    f.close()
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("dont have permision")
except FileExistsError:
    print("file does not exist")
except:
    print("unexcepted error while reading")
        
    
            
        