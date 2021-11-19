# <<<<<<<<<<<<<<[ "__init__ " function concept]>>>>>>>>>>>>>>>>>>>>>

# class Student:
#     def __init__(self):
#         self.name="Sudeep"
#         self.rollNumber=12



# s1=Student()
# # s1.name="sudeep"
# # s1.rollNumber=12
# print(s1.__dict__)

# s2=Student()
# # s2.name="priyanshu"
# # s2.rollNumber=13

# print(s2.__dict__)


# the __dict__ of both the s1 and s2 is same............!!!!!!!!


# ------ --  - -  -  - - -  - - -  - -  - - - -  - -  - - -  - -  - - - -  - -  - -  - -  -  - -  - - -  - - - - -  - - - 


class Student:
    def __init__(self,name,rollNumber):
        self.name=name
        self.rollNumber=rollNumber
        print(self.name)
        print(self.rollNumber)
    def __del__(self):
        print("welcome to destructor");

s1=Student("sudeep",12)
# print(s1.__dict__)

s2=Student("priyanshu",13)
# print(s2.__dict__)

s3=Student("Kumar",14) # here we are passing name and rollNumber with the object itself...!
                       # here we are passing 3 arguments "name and rollNumber explicitely" and "object itself implicitely"...!
                       # so we have to also write 3 argument in "__init__" function corresponding to this...!!!

# print(s3.__dict__)

# note:--- the number of argument passed alogwith the object itself must be equal to the number of argument in the "__init__" function 
#          alongwith the "self" ...........!!!!!!!!

del s1
del s2
del s3
