class Student:
    passingPercentage=80      # class attribute
    def studentDetails(self):
        self.name="Sudeep"    # it is a instance attribute
        print(self.name)

        # percentage=80
        self.percentage=80
        print(self.percentage)
        pass


    def isPassed(self):
        # if percentage>Student.passingPercentage:   # here if we run the output will be percentage is not defined as it is in the scope 
                                                   # studentDetails() function only......!!!!!!!!!
            # print("student is passed")

        if self.percentage>Student.passingPercentage: # here if we run the output will be fine because now it is an instance attribute!
            print("student is passed")
        else:
            print("student is not passed")


s1=Student()
s1.studentDetails()
Student.studentDetails(s1)    # it is same as the "s1.studentDetails()"
# class_name.function(object_name)
s1.isPassed()

# note :-- when we call a function like above then by default then oject by which it is called is passed as argument so if we want to
#          execute that function we have to give a argument in the function definition for that passed object. we can give any name to it
#          but it is a very strong convenction in python that it should be named as "self" there self notify the object itself is the 
#          argument by which the function is being called..!!!!!!!!!!!!!!!!!!!!



# self.name is the instance attribute means it is accessible till the life time of the instance
# whereas the percentage is restricted only inside the scope of the function there.........!!!

