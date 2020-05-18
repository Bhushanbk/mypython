name=["bhushan","ravi","darshan","sadaqt"]
roll_no=[4,3,21,1]
marks=[40,50,60,70]
mapped=zip(name,roll_no,marks)
mapped=list(mapped)
print("the zipped result is:",end=" ")
print(mapped)
print("\n")
namz,roll_noz,marksz=zip(*mapped)
print("the unzipped result \n",end=" ")
print("names",end=" ")
print(namz)
print("roll_no",end=" ")
print(roll_noz)
print("mark",end=" ")
print(marksz)