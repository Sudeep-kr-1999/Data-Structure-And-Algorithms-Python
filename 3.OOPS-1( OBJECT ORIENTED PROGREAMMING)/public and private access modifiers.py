# <<<<<<<<<<<<[ public and private access modifiers]>>>>>>>>>>>>>>>>>>>>>>>>


from datetime import date
class Student:
    # passingPercentage=40
    __passingPercentage=40     # making class variable as the private variables............!!!!!!!!!!
    def __init__(self,name,age=15,percentage=80):
        # self.name=name
        self.__name=name          # here now name become the private variable as we place "__"(underscore underscore ) before its name...!!!!
        self.age=age
        self.percentage=percentage

    def studentDetails(self):
        print("Name=",self.__name)
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


s1=Student("Parikh")
# print(s1.name)        # it will show error when name is private in the class
# print(s1.__name)      # it will show error when name is private in the class
# s1.name="Ankush"   # here we can access and change also the class data because it is now / by default public....!!!
# print(s1.name)
# s1.age=21          # here we can access and change also the class data because it is now / by default public....!!!
# print(s1.age)
# s1.studentDetails()          # this is allowed because this is the part of the class and have access to all variables inside the class..!!!

print(s1._Student__name)   # it is called "name mangling" so  by this way we can access private elements of the class outside the class..!!
print(s1._Student__passingPercentage)         # by using "name mangling concept"............!!!!!
print(Student._Student__passingPercentage)    #note:--- for class attribute we can use class name in place of object name.
                                               #       here "Student"in place of "s1"...!!!!
# print(Student._Student__name)             # it is the error because name is not the class attribute...............!!!!!!!!!!!!!

# # note:--- we donot want that our class variable goes under any change outside the class so to achieve this we make that variables as private
#            placing "__"(underscore underscore 2 times) before that variable name. after doing this that variable can only be accessed under the
#            clss not directly from outside the class...!!!!..........same logic in case of functions...............!!!!!!!!!!


                             #  <<<<<<<<<<<<<<<[ VERY VERY IMPORTANT NOTE]>>>>>>>>>>>>>>>>>>>>>>>
# NOTE:----------> THERE IS A PARTICULAR WAY OF ACCESSING PRIVATE MEMBERS OUTSIDE THE CLASS ....PYTHON HAS A WAY CALLED "NAME MANGLING"...!
#                  THE WAY OF WRITING IS ["object._class_name__variable_name"].!!!



