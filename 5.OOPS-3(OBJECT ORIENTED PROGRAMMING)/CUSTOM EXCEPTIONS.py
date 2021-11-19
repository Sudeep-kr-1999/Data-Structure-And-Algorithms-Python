# <<<<<<<<<<<<<<<<<<<<<<<<<<<[ CUSTOM EXCEPTIONS]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# while True:
#     try:
#         n=input("enter the numerator :")
#         num=int(n)

#         n=input("enter the denominator : ")
#         den=int(n)

#         if den==0:
#             raise ZeroDivisionError    # in output we will not print "hi".. it will handle zero division error because we raise this exception
#                                       # by our own here by giving the conditions..........!!!!(coustom exceptions)!!!!!!!!!! ( important)!!!
#                                       # we use "raise keyword " to raise the exception.........!!!!!!!!!
#         print("hi")

#         value=num/den
#         print(value)
#         break

#     # except (ValueError,ZeroDivisionError):        # handle multiple exception.............!!!!!!!!!!
#     #     print("numerator and denominator should be integers")


#     except (ValueError):        # handle multiple exception.............!!!!!!!!!!
#         print("numerator and denominator should be integers")


#     except ZeroDivisionError:
#         print("Denominator should not be zero")

# ---- - -  - -  -  - - - -  - -   - - - - -  - - - - -  - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# IN PYTHON WE CAN MAKE OUR OWN EXCEPTION WHICH ARE NOT DEFAULT IN THE PYTHON LANGUAGE.........!!!!!!!!
# SINCE WE MAKE OUR OWN EXCEPTION WE CAN ALSO HANDLE THOSE EXCEPTIONS............!!!!!!!!!!!!!


class ZeroDenominatorError(Exception):      # making our own exception as name "ZeroDenominatorError"..........!!!!
                                           # here "Exception class " has inbuilt"__init__" function which take message as argument and raise
                                           # exception.................!!!!!!!!!!!
    pass

while True:
    try:
        n=input("enter the numerator :")
        num=int(n)

        n=input("enter the denominator : ")
        den=int(n)

        if den==0:
            raise ZeroDenominatorError("Denominator Should Not Be Zero")
            # raise ZeroDenominatorError



        # // it will raise the exception like this in terminal //
        # raise ZeroDenominatorError("Denominator Should Not Be Zero")
        # # __main__.ZeroDenominatorError: Denominator Should Not Be Zero

        value=num/den
        print(value)
        break

    except (ValueError):
        print("numerator and denominator should be integers")


    except ZeroDivisionError:
        print("Division by Zero Is Not Allowed")


    except ZeroDenominatorError:            # handling our own exception.............!!!!!!!!!!!!!!!!
        print("ZeroDenominatorError is raised")

