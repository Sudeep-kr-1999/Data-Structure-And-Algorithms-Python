# <<<<<<<<<<<<<<<<<<<<<<<<<[ OPERATOR OVERLOADING IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import math
class point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def __str__(self):
        return "This point is at (" + str(self.__x) +","+str(self.__y) +")"

    def __add__(self,point_object):  # here self will be call for "p1" and "p2" will be a point object....!!!!!
        return point(self.__x+point_object.__x,self.__y+point_object.__y)
    def __lt__(self,point_object):
        return math.sqrt(self.__x**2 +self.__y**2) < math.sqrt(point_object.__x**2 +point_object.__y**2)
        # here we compare the distance of co-ordinate from the origin..............!!!!!!!!!!!!!!!!!!!!


p1=point(1,2)
p2=point(3,4)
p3=p1+p2
print(p3)
print(p1<p2)


