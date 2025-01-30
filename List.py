mylist=['Kishore', '16', 'Nellore', 'SDET']
#print(mylist)
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])
#print(mylist[1:3])#String replacing
#print(mylist[1:-3]) #string slicing

mylist.append('Reddy')# adding the string in the list
mylist.remove('SDET')# removing the list
print(mylist)
for x in mylist: #printing the elements in the list
    print(x)
    
for x in enumerate(mylist): #printing the elements in the list with index
    print(x)
    
for index, value in enumerate(mylist): #printing the elements in the list with index
    print(index, value)
    
    print(len("Kishore"))
    
    #mytuple=('17', '16', '7', 'Kishore')# if declare tuple we cannot change or modify the values
    mytuple=(67,)
    print(mytuple)

name='Kedhar'
print(''.join(reversed(name)))
#print(name[::-1]) # string reverse logic
name.upper
print(name)