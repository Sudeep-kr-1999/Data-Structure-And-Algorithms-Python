# <<<<<<<<<<<<<<<<<<<<<<<[ EXCEPT FUNCTIONALITY IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class ZeroDenominatorError(Exception):    # HERE WE INHERIT FROM CLASS EXCEPTION................!!!!!!!!!1
class ZeroDenominatorError(ZeroDivisionError):    #we can also inherit from the class "ZeroDivisionError" as well...........!!!!!!
    pass

while True:
    try:
        n=input("enter the numerator :")
        num=int(n)

        n=input("enter the denominator : ")
        den=int(n)

        if den==0:
            raise ZeroDenominatorError("Denominator Should Not Be Zero")

        value=num/den
        print(value)
        break

    except (ValueError):
        print("numerator and denominator should be integers")


    except ZeroDenominatorError:
        print("ZeroDenominatorError is raised")

    # except:
    #     print("there is some exception")   # if you execute the code right here you will get the error that default except should be at last..!


    except ZeroDivisionError:
        print("Division by Zero Is Not Allowed")


    # except ZeroDenominatorError:
    #     print("ZeroDenominatorError is raised")


    except:
        print("THERE IS SOME EXCEPTION")         # HERE DEFAULT EXCEPT IS IN LAST POSITION SO WE DONOT GET ANY TYPE OF ERROR.............!!
                                                # SO IF NON OF THE ABOVE ERROR WILL COME IT WILL GO TO THIS EXCEPT......!!!!!





# very very important concept below.........!!!!!!!!!!!!!!!!!
# note:------------>>>>  in the above code  ZeroDenominatorError is a child class of ZeroDivisionError and ZeroDivisionError is the parent class
#                        of ZeroDenominatorError so jab ZeroDenominatorError exception raise hoga to wo except block mein aayega aur line se
#                        or order way mein starting se end tak ZeroDenominatorError search krega but jaise hi wo search krte krte ZeroDivisionError
#                        pr aayega to since ZeroDenominatorError is a ZeroDivisionError or in other words ZeroDenominatorError is the child class
#                        of ZeroDivisionError to wo parent ke pass jaakr ZeroDivisionError waale message ko print kr dega!!


#                        but agar hum order change krde mtlb in above code hum ZeroDivisionError(handling) ko ZeroDenominatorError(handling) ke
#                        neeche le aaye to use ZeroDenominatorError pehle milega to use parent ke paas jaane ke zaroorat nhi padegi aur ZeroDenominatorError
#                        (handling) wala message print ho jayega...............!!!!!!!!!!!!



# # in simple language agar exception ka handling search krte krte kisi ko agr apne khud ke handling se pehle wo handling mil jaaye jo uske
#  parent class k ha to uska handling execute kr jaayega kyuki jiski handling hum search kr rhe h wo us parent class ka hi ek part h but agr
#   khud ki hi handling pehle mil jaaye to parent ke paas jaane ki zaroorat hi  nhi padegi khud ki hi handling execute ho jayegi means parent
# #   or child mein jo pehle aayega wo hi execute ho jayega......................!!!!!!!!!!!!!!!!!