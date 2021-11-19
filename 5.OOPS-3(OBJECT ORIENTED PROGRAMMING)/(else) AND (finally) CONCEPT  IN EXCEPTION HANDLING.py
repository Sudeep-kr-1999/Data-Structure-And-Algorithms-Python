        # <<<<<<<<<<<<<<<<<[ ELSE AND FINALLY CONCEPT IN EXCEPTION HANDLING]>>>>>>>>>>>>>>>>>>>>>>>>

# ELSE:-------> IF WE DONOT GET ANY EXCEPTION ELSE BLOCK IS BEING EXECUTED.............!!!!!!!!!!!!!!
# FINALLY -------> IT IS AGAIN A KEYWORD AND IT WILL ALWAYS COME AT THE LAST OF THE EXCEPTION HANDLING......!
                   # order is:  (try-------> except---------> finally)  OR  (try--------> except----------> else ----------> finally)
                   # "finally" code is definitely excuted doesnot matter wehther exception is raised or not .........it does not matter....!!!!


class ZeroDenominatorError(ZeroDivisionError):
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

    except (ValueError):
        print("numerator and denominator should be integers")


    except ZeroDenominatorError:
        print("ZeroDenominatorError is raised")


    except ZeroDivisionError:
        print("Division by Zero Is Not Allowed")


    except:
        print("THERE IS SOME EXCEPTION")


    else:
        print(value)
        break


    finally:
        print("exception may or may not be raised")



# note:---------> there is another keyword that is "finally" and it will come always at the last of the exception handling.......!!!!!
                #  order is:  (try-------> except---------> finally)  OR  (try--------> except----------> else ----------> finally)
