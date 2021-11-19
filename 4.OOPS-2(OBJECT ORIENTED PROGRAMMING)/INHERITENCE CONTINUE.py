
class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.__maxSpeed=maxSpeed   # here maxSpeed is a private member of this class.........!!!!!!!!!!

        # NOTE:--- HERE CAR DONOT ABLE TO INHERIT "maxSpeed" from the vehicle class as it is the private member of the vehicle class...!!!!!!!

    # getter and setter logic in inheritence............!!!!!!!
    def getmaxspeed(self):      # getter function.........!!!!!
        return self.__maxSpeed


    def setmaxspeed(self,maxSpeed): # setter function..............!!!!!!!!!!!
        self.__maxSpeed=maxSpeed


    def print(self):
        print("Color : ",self.color)
        print("MaxSpeed : ",self.__maxSpeed)




class car(vehicle):
    def __init__(self, color, maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible


    def printCar(self):
        super().print()            # printing with the help of print function in the base class.............!!!!!!!!!!!
        self.print()                # in this case super().print is same as self.print() but not always..................!!!!!!!!!!!1
        # print("Color : ",self.color)
        # # print("MaxSpeed : ",self.maxSpeed)      # this will not work since "maxSpeed" is now a private member..!
        # print("MaxSpeed : ",self.getmaxspeed())       # this will work as we use getter and setter logic to access the private members.....!!!
        print("NumGears : ",self.numGears)
        print("IsConvertible : ",self.isConvertible)

c=car("red",15,3,False)
c.printCar()
