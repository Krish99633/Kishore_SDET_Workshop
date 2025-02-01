
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def printCar(self):
        print("Brand:", self.brand)
        print("year:", str(self.year))
        
#single inheritance

class Swift(Car):
    def __init__(self, model, type, name):
       self.model = model
       self.type = type
       self.name = name
       
    def printSwift(self):
        print("Model:",self.model)
        print("Type:",self.type)
        print("Name:",self.name)
        
class Kia:
    def __init__(self,color):
        self.color = color
        
    def printKia(self):
        print("Color:",self.color)
        
#M5__>Swif__>Kia
        
class M5(Swift,Kia):
    def __init__(self, color, engine):
        self.color= color
        self.engine = engine
        
    def printM5(self):
        print("Color:",self.color)
        print("Engine:",self.engine)
        
        
    def printKia(self):
        self.color = "Meron Red"
        return super().printKia()
    
m5 = M5("Red","DDIS")
m5.printM5()
m5.printKia()