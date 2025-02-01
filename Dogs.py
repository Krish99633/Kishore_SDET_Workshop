
#inheritance examples

class Dog:
    def __init__(self,name):
        self.name= name
        
    def bark1(self):
        return f"{self.name} says woof!" # used f string to print the string values
    
class GoldenRetriver(Dog):
    
    def __init__(self, name,color):
        self.color = color
        super().__init__(name)
        
    def bark(self):
        return f"{self.name} says woof! and is {self.color} in color"
 #Main class in python to execute above   
myGoldenRetriver = GoldenRetriver("Buddy","Golden")
print(myGoldenRetriver.bark())
print(myGoldenRetriver.bark1())