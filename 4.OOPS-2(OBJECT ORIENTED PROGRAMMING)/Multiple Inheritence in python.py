# <<<<<<<<<<<<<<<<<<[ MULTIPLE INHERITENCE IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>

class mother:
    def __init__(self):
        self.name="Manju"
    def print(self):
        print("Print of Mother Called ")

class father:
    def __init__(self):
        self.name="Ajay"
    def print(self):
         print("Print of Father Called ")

# class Child(father,mother):   #it will first print the print function of father then mother as per the order..............!!!
class Child(mother,father):   # it will first print the print function of mother then father as per the order........!!!!!!
    # def __init__(self,name):
    #     self.name=name

    def __init__(self):
        super().__init__()   # here super() go to the base class and it will print the message according to the order of inheriting here mother
                             # is first in order so "Manju" is printed for self.name..................!!!!!!!!!!

    def printChild(self):
        print("Name of child is : ",self.name)



c=Child()
c.printChild()
c.print()    # it return in the order in which class base class is used to inherit!!!!!!!
             # here in child class we inherit father first and then mother so it will print the print function of father first and then mother
             # if we change the order of inheriting means now we inherit mother first then after father the print function of mother will execute
            #  first then father..............!!!!!!!!!!!( important logic )!!!!!!!!!


