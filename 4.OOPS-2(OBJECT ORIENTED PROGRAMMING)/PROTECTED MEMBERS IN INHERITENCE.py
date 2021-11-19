# <<<<<<<<<<<<<<<<<<<[ PROTECTED MEMBERS IN INHERITENCE IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>

# note:------>>1. protected members are declared by placing "_" (single underscore) before the name of the variable................!!!!!
            #  2. it has been asumed that protected member concept is used in the case of subclasses.............!!!!
            #  3. protected members are accessible in the subclasses of a parent classes and outside the classes also just like public members!!
class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self._maxSpeed=maxSpeed        #here we make the maxSpeed protected everywhere by placing single underscore before its variable name..!!


    def getmaxspeed(self):
        return self._maxSpeed


    def setmaxspeed(self,maxSpeed):
        self._maxSpeed=maxSpeed

    def print(self):
        print("Color : ",self.color)
        print("MaxSpeed : ",self._maxSpeed)

class car(vehicle):
    def __init__(self, color, maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible

    def print(self):
        # super().print()
        print("Color : ",self.color)
        print("MaxSpeed : ",self._maxSpeed)
        print("NumGears : ",self.numGears)
        print("IsConvertible : ",self.isConvertible)

# c=car("red",15,3,False)
# c.print()
v=vehicle("red",18)
v.print()
v._maxSpeed=19        # here we come to know in python protected members are just like public members as we are able t access it outside the
                      # class and also able to change it ............................!!!!!!!!!!!!!!!!!!!!!!!!!!!( very very important)...!!
v.print()




# note:------- python provide this logic of protected members because  user should come to know that yes!!!!!! this variable is  protected and
#              we should use it in any class but we should take care that we would change it as minimum as possible !!!!! we can change it whole
#              but we should not used to change the protected members....................more and more..........!!!!( very very important)!!!!