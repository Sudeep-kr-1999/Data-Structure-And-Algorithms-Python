
# <<<<<<<<<<<<<<<<<<<<<<<<<[ ABSTRACT CLASS CONCEPT IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>

from abc import ABC,abstractmethod

class Automobile(ABC):

    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
        print("Automobile created")


    @abstractmethod
    def start(self):
        print("start of Automobile called")

        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_no_of_wheels(self):
        return self.no_of_wheels

class car(Automobile):
    # def __init__(self,name):
    #     print("CAR CREATED")
    #     self.name=name

    def start(self):
        super().start()
        print("start of car called")

        pass

    def stop(self):
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

class bus(Automobile):
    # def __init__(self,name):
    #     print("BUS CREATED")
    #     self.name=name

    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

c=car(4)           # since car has no "__init__" so it will go to the "__init__" of parent class that is automobile
b=bus(8)            # since bus has no "__init__" so it will go to the "__init__" of parent class that is automobile
# b=bus("DELHI METRO BUS")
# c=car("HONDA")
# c.start()
print(c.get_no_of_wheels())
print(b.get_no_of_wheels())

# note:--- > it is not necessary that abstractmethod donot have any code or you cannot run that code we can run that code as per our use...!
