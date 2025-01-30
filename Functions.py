def div(a,b):
    return a/b
print(div(b=2,a=4))
#print(div(2,0))

def id(name,uid="00"):
    print(uid,name)
id(name='kishore',uid="123")
id(name='kedhar')

#printing the parameters

def myfunc(*args):
    
    for x in args:
        print(x)
myfunc(1,2,3,4,5)        

def myfunc2(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
        
myfunc2(name='kishore',age=29,city='Chennai')