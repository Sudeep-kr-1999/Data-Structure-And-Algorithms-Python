# <<<<<<<<<<<<<<<<<<<<<<[ OBJECT CLASS CONCEPT IN PYTHON]>>>>>>>>>>>>>>>>>>>>

# NOTE:--- 1. GENERALLY EACH CLASS INHERIT FROM OBJECT CLASS BY DEFAULT.........!!!

#          THERE ARE 3 METHODS PROVIDED BY OBJECT CLASS:---------
#          1. (__new__)------> this is used to create new objects
#          2. (__init__)-----> this is used to initialize the objects
#          3. (__str__)-------> it is used to give the description of the object of the class jis tarah user demand krege.....!!!!(vvi).


# note:-------> class Circle: is same as class Circle(object):

# class Circle:
# class Circle(object):
#     def __init__(self,radius):
#         self.radius=radius

# c=Circle(3)
# print(c)       # it will give you the output as:(<__main__.Circle object at 0x011B52C8>)!!!.... it also contain address of the object..!


# ---  - - -  -  - - -  - -  - - - - - -  - - - -  - - - - - - - -  - - - - - -  - - - - - - - - -  - - - - - - - - - - - - - - - -  - - -


class Circle(object):
    def __init__(self,radius):
        self.radius=radius


    def __str__(self):
        return"THIS IS A CIRCLE CLASS WHICH TAKE RADIUS AS A ARGUMENT"


c=Circle(3)
print(c)       # it will give you the output as:(THIS IS A CIRCLE CLASS WHICH TAKE RADIUS AS A ARGUMENT)

# NOTE:---- > WHEN WE USED FUNCITON (__str__) then we will be able to give the description of an object of our own it will not happen by default
#            and print the class of object and its address instead it will print what we provide it in the description inside the "__str__"
#            function.!

