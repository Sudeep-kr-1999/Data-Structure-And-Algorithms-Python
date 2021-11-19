# <<<<<<<<<<<<<<<<<<<<<<<<<[ HANDLING MULTIPLE EXCEPTION]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

while True:
    try:
        n=input("enter the numerator :")
        num=int(n)

        n=input("enter the denominator : ")
        den=int(n)

        value=num/den
        print(value)
        break

    # except (ValueError,ZeroDivisionError):        # handle multiple exception.............!!!!!!!!!!
    #     print("numerator and denominator should be integers")


    except (ValueError):        # handle multiple exception.............!!!!!!!!!!
        print("numerator and denominator should be integers")


    except ZeroDivisionError:
        print("Denominator should not be zero")



