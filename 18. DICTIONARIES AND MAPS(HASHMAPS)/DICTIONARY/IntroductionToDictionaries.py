# <<<<<<<<<<<<<<<<<<<<<<<<[ INTRODUCTION TO DICTIONARIES]>>>>>>>>>>>>>>>>>>>>


# Note:----> DICTIONARIES ARE MUTABLE....!!!!!!!!!!!!!!!

a={}   # creating dictionary
print(type(a))
a={"the":1,"a":5,10000:"abc"}
print(a)
print("length of dictionary ""a"" is :",len(a))

b=a.copy()
print(b)


c=dict([("the",3),("a",10),(2,3)])  # inside dict() there is a list having key values pairs of the dictionaries!
print(c)

d=dict.fromkeys(["abc",32,4],10)  #fromkeys(arg1,arg2) fromkeys() takes 2 argument first argument is the list containing all the keys we want
                                #   and the second argument is the value which get assigned corresponding to all the  keys of the dictionaries.

                                #   Note:-- > if we donot pass second argument in the fromkeys() function then the all keys in the dictionaries
                                #              having the default value that is None.!
print(d)
