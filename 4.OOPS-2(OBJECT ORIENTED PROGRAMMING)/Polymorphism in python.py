# <<<<<<<<<<<<<<<<<<<<<<[ POLYMORPHISM IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>


class vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.__maxSpeed=maxSpeed


    def getmaxspeed(self):
        return self.__maxSpeed


    def setmaxspeed(self,maxSpeed):
        self.__maxSpeed=maxSpeed


    def print(self):                  # one print function is present here!!!!!!!!!!!!!!!!!
        print("Color : ",self.color)
        print("MaxSpeed : ",self.__maxSpeed)




class car(vehicle):
    def __init__(self, color, maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible


    def print(self):                # another print function is present here...............!!!!!!!
        super().print()            # it will work fine here..................!!!!!!!!!!!!!!!!!!!
        # self.print()    # IF WE PROVIDE THIS self.print() it will call itself again and again and since it has no base case it will stuck in
                        #   recursion...............!!!!!!!!!!!!!!!!!
        print("NumGears : ",self.numGears)
        print("IsConvertible : ",self.isConvertible)


#   NOTE:-------- HERE THE PRINT FUNCTION INSIDE THE SUBCLASS IS PRINTED BUT IF WE COMMENT OUT THIS PRINT FUNCTION THEN THE PRINT FUNCTION INSIDE
#                THE SUPER CLASS WILL BE PRINTED IN THE OUTPUT TERMINAL....................!!!!!!!!!!!!!!
c=car("red",15,3,False)
c.print()

# # it we execute it by commenting out self.print() or super().print() in the print section in the derived class then that function will get
#   executed which come under the type of object by which it is called....!!!!!!!!!!!!!

#   # here in this case "c" is a object of class car........ so print function under the car class has been printed not the superclass of it
#     that is vehicle class...................!!!!!!!!!!!

# note:------- at first if two function with same name  are present one in the base class and second in the derived class then at first the
            #    function in the derived class is being called.........!!( very very important note)!!!! and if it is not there the function in
            #  the superclass will be called ...............!!!!!!!!!


# IN ONE WORD THE ORDER IS (FIRST ITSELF)..........(THEN ITS PARENT)..............(THEN ITS GRAND PARENT)...........THEN SO ON..........!!!!!!