# <<<<<<<<<<<<<<<<<<<[ ATTRIBUTES IN OOPS IN PYTHON]>>>>>>>>>>>>

class Student:
    pass
    # name=""
    # rollNumber=12
    # above is the way how we do in c++ and java but python has a very different way!!!

s1=Student()
s2=Student()
s3=Student()

s1.name="Sudeep"
s2.rollNumber=12
s3.name="Rohan"
s3.rollNumber=14

# print(s1.name)
# print(s2.rollNumber)
# print(s3.name)
# print(s3.rollNumber)
# print(s2.name)  # it gives us the error because s2 donot have name in it...!!!!

#- -  - - - -  - - - - -  -  - -  - - - - -  - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - -- - -  - - - - - - - - 


# "__dict__" functionality it give us the information about objects that which objects contains which attributes.
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)


#- -  - - - -  - - - - -  -  - -  - - - - -  - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - -- - -  - - - - - - - - 


# " hasattr() functions "
# it takes 2 arguments first the object in which we want to check and the second the key we want to check..!
# it check it that attribute is present in the given object or not..!!!!
# print(hasattr(s1,"name"))    #it returns the boolean means "True" or "False"!
# print(hasattr(s2,"name"))



#- -  - - - -  - - - - -  -  - -  - - - - -  - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - -- - -  - - - - - - - - 

# "getattr() functionality"
# it gives the value corresponding to the given attribute and the given objects as its arguments....!!

# print(getattr(s1,"name"))
# print(getattr(s2,"name"))   # it give us the error because s2 donot has any name

# print(getattr(s2,"name","sudeep")
# # this third argument is to handle the error if the value corresponding to the second argument attribute is available then we get the 
# # right ans but if it is  not available in the given object then we get the third argument as the output not the error.....!!!!!


#- -  - - - -  - - - - -  -  - -  - - - - -  - - -  - - - - - - - - -  - - - - - - - - - - - - - - - - - - -- - -  - - - - - - - - 

# "delattr() functionality"
# it will delete the given attribute as its argument from the object passed under it as the argument..!!

delattr(s1,"name")
print(s1.__dict__)   # it show you nothing because name attribute is deleted above by using delattr() functionality.....!!!!

 



