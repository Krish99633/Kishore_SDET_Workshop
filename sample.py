class Emp:
    # Constructor
    def __init__(self, name, exp, role):
        self.name = name
        self.exp = exp
        self.role = role
    

    def printEmp(self):
        print("Name:", self.name)
        print("Experience:", self.exp)
        print("Role:", self.role)


emp1 = Emp("Kedhar", 2, "My Boy")
emp1.printEmp()