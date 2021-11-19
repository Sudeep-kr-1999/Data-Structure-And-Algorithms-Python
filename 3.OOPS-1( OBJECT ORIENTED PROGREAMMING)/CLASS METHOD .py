# <<<<<<<<<<<<<<<<<<<<<<<[ class methods in python]>>>>>>>>>>>>>>>>>>>>>>>>
from datetime import date
class Student:
    passingPercentage=40
    def __init__(self,name,age=15,percentage=80):
        self.name=name
        self.age=age
        self.percentage=percentage

    @classmethod
    def fromBirthYear(cls,name,year,percentage):
        return cls(name,date.today().year-year,percentage)
    def studentDetails(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Percentage=",self.percentage)
        pass

    def isPassed(self):
        if self.percentage>Student.passingPercentage:
            print("Student is passed")
        else:
            print("student is not passed")

    @staticmethod
    def welcomeToSchool():
        print("hey!! welcome to school")


    @staticmethod
    def isTeen(age):
        return age>16

# s1=Student("Parikh")
s1=Student.fromBirthYear("Sudeep",1999,75)
s1.studentDetails()
# s1.isPassed()



# note:------- in class methods we will be returning objects of the class
#              the class method is also called factory methods...!!!
#              for class method we used the decorator i.e "@classmethod"
#              it must have first argument as "class"
#             def method_name(class_name,__,__,__..)
