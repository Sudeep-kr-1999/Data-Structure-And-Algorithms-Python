# <<<<<<<<<<<<<<<<<<<<<<<<<[ ABSTRACT CLASS CONCEPT IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>

from abc import ABC,abstractmethod

class Automobile(ABC):

    def __init__(self):
        print("Automobile created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# c=Automobile()          # // output//
                        # c=Automobile()
                        # TypeError: Can't instantiate abstract class Automobile with abstract methods drive, start, stop

# note:-----> in astract class if we set  even a single method as "@abstractmethod" then we are not able to make the object of that class!
            # ( its the property of abstact class that is it donot have any objects instantiate...!!!!)
            # it you remove the "@abstractmethod" from evrywhere you can able to create the object of that class......!!!!!!!!

class car(Automobile):

    # def __init__(self,name):
    #     print("Car created")
    #     self.name=name


# NOTE:----->> WHEN "__init__" is there the object called the "__init__"but if we remove the "__init__"then "__init__" of parent class is called!



# c=car ("HONDA")               # //OUTPUT//
                              # c=car ("HONDA")
                              # TypeError: Can't instantiate abstract class car with abstract methods drive, start, stop

# NOTE:- IF WE INHERIT FROM ABSTRACT CLASS THEN WE MUST HAVE TO IMPLEMENT  ALL THE "abstractmethod" INSIDE THE ABSTRACT CLASS............!!!!

    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass

# c=car("HONDA")        # NOW AFTER IMPLEMENTING ALL THE  "abstractmethod" IT WILL WORK ABSOLUTELY FINE......!!
                      # // OUTPUT WITH "__init__" in the derived class i.e, car class.!!!//
                      # Car created

# c=car()              # // OUTPUT WITHOUT  "__init__" in the derived class i.e, car class.!!!//
                      #  Automobile created

class bus(Automobile):
    def __init__(self,name):
        print("BUS CREATED")
        self.name=name

    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass

b=bus("DELHI METRO BUS")