# <<<<<<<<<<<<<<<<[ ADDING, UPDATING,REMOVING DATA FROM THE DICTIONARY]>>>>>>>>>>>>>>>>>>>>>>>>>>

a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a)
a["tuple"]=(1,2,3)   # adding data to the dictionary!
print(a)

a[1]=10 # updating the data of the value corresponding to the key given here!!

b={3:5,"the":4,2:100}
a.update(b)   # if something is common "b" value would be used else they both just adds up!!
print(a)

print(a.pop("tuple"))  # pop() require the key of the data which we want to remove from the dictionary!
                       # pop() function itself return the value associated with the key which is going to be deleted...!!
print(a)

del a[1]   # it will delete key 1 from the dictionary!
a.clear()  # it will clear all data from the dictionary but the dictionary is still there..!
del a       #it will deleter all the dictionary itself!




