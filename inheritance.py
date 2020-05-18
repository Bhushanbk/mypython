class Person:
    name=""
    age=0
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge
    def display(self):
        print("Name is:",self.name)
        print("age is:",self.age)
class student(Person):
    studentId=""
    fess=0.0
    def __init__(self,studentName,studentAge,studentId,fees):
        Person.__init__(self,studentName,studentAge)
        self.studentId=studentId
        self.fees=fees
    def getId(self):
        return self.studentId
    def getFee(self):
        return self.fees
print("person details are")
person=Person("ricky ponting",50)
person.display()
print("student details")
student=student("gagungly",50,"129",500000)
student.display()
print("student Id:",student.getId()) 
print("student Fee:",student.getFee())
print(">>>>>>>>>>>>>>")   