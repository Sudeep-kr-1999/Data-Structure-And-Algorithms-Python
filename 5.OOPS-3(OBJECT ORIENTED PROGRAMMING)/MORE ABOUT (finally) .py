# <<<<<<<<<<<<<<<<<<<<[ UNDERSTANDING FUNCTIONALITY OF "finally"]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


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
        print(num)
        print(den)
        print(value)
        print("exception may or may not be raised")

# note:----------> "finally" ke andar koi bhi value tb print hogi jab wo achievable hogi agr uske code tak achieve nhi kr paayege to error show
#                  krega...........!!!!!!!!!!!!!!!!   ( important logic)!!!!!!!!!!!!!!!!

                   # jha pr exception aayega ya galat input aayega wha se aage ka code ka koi sence nhi rhega kyuki wo direct exception ke andar
                #    chala jayega ..................!
