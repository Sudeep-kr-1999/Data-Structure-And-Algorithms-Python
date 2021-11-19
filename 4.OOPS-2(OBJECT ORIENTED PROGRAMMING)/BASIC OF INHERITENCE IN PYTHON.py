# <<<<<<<<<<<<<<<<<<<<<<<<[ BASIC OF INHERITENCE IN PYTHON ]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.maxSpeed=maxSpeed

class car(vehicle):
    # here we should also provide constructor argument as in vehicle to initialize it then after we give argument for the car class..!

    def __init__(self, color, maxSpeed,numGears,isConvertible):
        # note:---> super() function  is used to inherit the property from the base class..............( very very important.!)

        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible

    def printCar(self):
        print("Color : ",self.color)
        print("MaxSpeed : ",self.maxSpeed)
        print("NumGears : ",self.numGears)
        print("IsConvertible : ",self.isConvertible)

c=car("red",15,3,False)
c.printCar()



# = = = = = = = = = = = = = = = = = = = = = = = =  = = = == = = = = = ==== = = = = = = = = == = = = = == = = = = = == = = = = == = = = == = = == = = == = = = = === =
# very very important concept............................!!!!!!!!!!!!!!!!!
# this will work perfectly.........................!!!!!!!!!!!!!!!!!!!
class a:
    __i=5
    print("hello i am from class a")
    print(__i)

class b:
    j=2
    print("hello i am from class b")
    print(j)
class c:
    k=2
    print("hello i am from class c")
    print(k)
