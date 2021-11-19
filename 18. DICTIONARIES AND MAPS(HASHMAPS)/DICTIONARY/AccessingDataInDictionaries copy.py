# <<<<<<<<<<<<<<<<<<<<[ ACCESSING DATA IN DICTIONARIES]>>>>>>>>>>>>>>>>>>>>>>

a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a)

# print(a[0])
# Note:---> we donot use indexing like that which are used in the list like a[0],a[2]....etc
            # instead we use the actual keys which are present in the dictionaries..!
#  line 5, in <module>
#     print(a[0])
# KeyError: 0

# accessing data in the dictionaries..!
print(a[1])
print(a[3])
print(a["list"])
print(a["dict"])
# print(a["li"])   # here we get an error because this key is not present in the dictionary !


print(a.get(1))
print(a.get(3))
print(a.get("list"))
print(a.get("dict"))
print(a.get("li"))   # here halaki "li" dictionary ki keys value mein present nhi h hume yha error nhi milega ye direct "None" return kr dega..!
print(a.get("li",0)) #note-----> get(arg1,arg2) here hum get() function mein 2 argument pass krte h fist argument for the key and second argument
                                #  for the value which it return when key donot exist in the dictionary!

                             #  means agar key dictionary mein present hoga to get() function key ke corresponding value ko return krega aur
                            #  agar key present nhi hoga to wo by default "None" return krega but agar key present nhi hoga aur humne arg2 ki
                            # value de rkhi hogi to "None" ke place pr wo arg2 wli value return krega........!!!! (very very important logic)!!


print(a.keys())
print(a.values())
print(a.items())


# for loop using dictionary:
for i in a:
       print(i,a[i])# here i is the keys in the dictionary


for i in a.values():  # passing through all the values!
   print(i)


print("list" in a)  #check whether key is present in the dictionary or not!!!!
print("li" in a)
print(2 in a)  # this is false because we donot check values we check keys and 2 here is the value not the key!

