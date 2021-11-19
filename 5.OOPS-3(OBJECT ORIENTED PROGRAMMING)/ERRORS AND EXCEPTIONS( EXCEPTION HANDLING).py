# <<<<<<<<<<<<<<<<<<[ errors and exceptions concept in python]>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# we made may type of errors in the program so by using this we learn how to handle those errors................!!!!!!!!!!

# n=input("enter the numerator :")
# num=int(n)

# n=input("enter the denominator : ")
# den=int(n)

# value=num/den
# print(value)

# note :----->> if you enter any string while inputing the value of numerator you will get the following error ...!!(in this case..!)
                #  line 6, in <module>
                #  num=int(n)
                #  ValueError: invalid literal for int() with base 10: 'abc'

# <<<<<<<<< ( IF WE HAVE TO HANDLE THESE KIND OF ERROR WE USE THE CONCEPT CALLED EXCEPTION HANDLING )>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!!!!

# - - - -  - -  - - - - -  - - -  - - - -  - - - - - - - - - - - - -  - - - - -- -  - - - - - - - - -  - - - - - - -  - - -  - -
            #   <<<<<<<<<<<<<<<<<<<[ EXCEPTION HANDLING OF THE ABOVE CODE]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
while True:       # jab tak value sahi nhi hoga input lete rhega aur jaise hi sahi input milega ye value print krke exit kr jaayega...!!!!!
    try:
        n=input("enter the numerator :")
        num=int(n)

        n=input("enter the denominator : ")
        den=int(n)

        value=num/den
        print(value)
        break

# except ValueError:           # now the value error is handled means if you make any error in values it would execute the except block instead of
#                             # showing us the error as above code...........!!!!!!!!!!!!!!!!!!!
#     print("Numerator and Denominators should be integers")


    except:             # if we donnot specify anything it will handle all the errors...................!!!!!!!!!!!!!(important)!
        print("numerator and denominator should be integers")

