# <<<<<<<<<<<<<<<<<[BASIC OF OOPS IN PYTHON]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class student:
    pass   # note:--- we cannot left the class empty so we use pass

s1=student()   # creating a object "s1" for student class
print(s1)
print(type(s1))
l=list()
print(type(l))

s2=student()
s3=student()
print(s2,s3)

# = = = = = = = = = = = = = = = = = = = = = = = =  = = = == = = = = = ==== = = = = = = = = == = = = = == = = = = = == = = = = == = = = == = = == = = == = = = = === =
# very very important concept............................!!!!!!!!!!!!!!!!!
# this will work perfectly.........................!!!!!!!!!!!!!!!!!!!
class a:
    __i=5
    print("hello i am from class a")
    print(__i)

class b:
    j=2
    print("hello i am from class b")
    print(j)
class c:
    k=2
    print("hello i am from class c")
    print(k)




