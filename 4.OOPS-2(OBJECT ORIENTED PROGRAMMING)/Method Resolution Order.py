# <<<<<<<<<<<<<<<<<<<<<[ METHOD RESOLUTION ORDER IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>


class mother:
    def __init__(self):
        self.name = "Manju"
        super().__init__()   # now as per resolution order the mother is already called so this statement will call the father class and give
        # the desired output..............!!!!!!!!!!!!!!( important!)

    def print(self):
        print("Print of Mother Called ")


class father:
    def __init__(self):
        self.name = "Ajay"
        super().__init__()   # now above the father class is already called so this statement will call the "object " and nothing will happen
        # right now...................!!!!!!!!!

    def print(self):
        print("Print of Father Called ")

# class Child(father,mother):   #it will first print the print function of father then mother as per the order..............!!!


class Child(mother, father):   # it will first print the print function of mother then father as per the order........!!!!!!
    # def __init__(self,name):
    #     self.name=name

    def __init__(self):
        super().__init__()   # here super() go to the base class and it will print the message according to the order of inheriting here mother
        # is first in order so "Manju" is printed for self.name..................!!!!!!!!!!

    def print(self):
        print("Name of child is : ", self.name)


c = Child()
c.print()  # ------>>> #IT WILL FIRST GO TO THE (CHILD CLASS)........ THEN (PARENT CLASS)......THEN (GRANDPARENT CLASS) ......AND SO ON!!!!!!!

# WE ALSO HAVE WAY TO CHECK THE ORDER IN WHICH THE FUCTION CALLING TAKE PLACE , IN THIS PROGRAMME THE ORDER OF PRINT FUNCTION CALL TAKE PLACE....
# THAT IS MENTION BELOW..!!

# (very very important function "mro()")
# // [<class '__main__.Child'>, <class '__main__.mother'>, <class '__main__.father'>, <class 'object'>] //
print(Child.mro())


# ============ = =  = = = = =  = = = = = =  = = =   = = = =  = = =  = = = = = = = = = = = = = =  = = = = == = = = = =  = ==  == = = = =  = = = = = = = = = = = =
class square:
    def area(self):
        side = int(input("Enter the value of side:"))
        # print(side*side)
        return side*side


class rectangle(square):
    def area(self):
        length = int(input("Enter the value of Length:"))
        breadth = int(input("Enter the value of Breadth:"))
        print(super().area())
        return length*breadth

obj = rectangle()
print(obj.area())
