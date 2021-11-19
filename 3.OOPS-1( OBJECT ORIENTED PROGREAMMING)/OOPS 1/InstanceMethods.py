# <<<<<<<<<<<<[ INSTANCE METHOD IN PYTHON]>>>>>>>>>>>>>>>>>>

class Student:
    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber

    def printStudent(self):
        print("My name is ",self.name, " and My roll no is: ",self.rollNumber)

s1=Student("Ankush",12)
# print(s1.__dict__)
# s1.printStudent()
Student.printStudent(s1)
