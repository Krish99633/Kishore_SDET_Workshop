

# Map like dict will support for colloection concepts using dict
mydict={
    'name':'Kishore',
    'age' :28,
    'City': 'Chennai'
}
mydict["exp"]=20
print(mydict)
mydict.pop("exp")
mydict.update({"exp":30})
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict["name"])
mytuple=(mydict)
print(mytuple)

for x,y in mydict.items(): # to print list of key value pairs
    print(x,y)
    
for exp, value in enumerate(mydict):
    print(exp, value)



#collection concept Set interface hear it is myset is un-ordered
myset={1,2,3,4,5,4,4,3,3,5}
myset.add(9)
myset.remove(5)
myset.discard(11) # fail safe method if it is not present it will neglect
myset.pop()
myset.update({10,11,12,13,14,14,5,5})
print(myset)
for x in myset:
    print(x)
    
#union & intersection function code
a={2,3,4}
b={1,2,6}

print(a.union(b))
print(a.intersection(b))