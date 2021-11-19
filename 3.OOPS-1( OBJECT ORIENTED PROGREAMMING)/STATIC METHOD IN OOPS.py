# <<<<<<<<<<<[ STATIC METHOD (class method) IN PYTHON]>>>>>>>>>>>>>>

class Student:
    passingPercentage=40

    def studentDetails(self):
        self.name="Sudeep"
        print(self.name)
        self.percentage=80
        print(self.percentage)
        pass
    
    def isPassed(self):
        if self.percentage>Student.passingPercentage:  # here we should write "Student.passingPercentage"( as it is the class attribute)!
            print("the student is passed")
        else:
            print("the student is not passed")
    
    @staticmethod  # this decorator will stop the by default passing of object at the time of function call....!!!
    def welcometoschool():    # due to decorator do not require to write self there........!!!
        print("hey welcome to school")


    
    # @staticmethod  # this decorator will stop the by default passing of object at the time of function call....!!!
    # def welcometoschool(self):   #if we write self here then it is expecting that you should pass self at the time of calling...(vvi)
    #     print("hey welcome to school")

s1=Student()
s1.studentDetails()
# Student.studentDetails(s1)
s1.isPassed()
s1.welcometoschool()
