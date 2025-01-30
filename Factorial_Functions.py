def sum(a,b):
    return a+b
result=sum(7,6)
print(result)

#factorial using if loop
def factorial(n):
    if n < 0:
        return "Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
if __name__ == "__main__":
    number = int(input("Enter positve number: "))
    print(f"The factorial of {number} is {factorial(number)}")
    
#factorial using isdigit() function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    X = input("Enter a value: ")
    if X.isdigit():
        num = int(X)   
        print("Factorial is: " + str(factorial(num)))
        break
    else:
        print("Please enter digits only.")
#Negative values finding factorial        
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    X = input("Enter a value: ")
    if X.lstrip('-').isdigit():  # This handles negative numbers as well
        num = int(X)
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial is: " + str(factorial(num)))
        break
    else:
        print("Please enter digits only.")
        
        
#Negative values should get the factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    X = input("Enter a value: ")
    try:
        num = int(X)
        if num < 0:
            num = abs(num)  # Convert negative to positive
        print("Factorial is: " + str(factorial(num)))
        break
    except ValueError:
        print("Please enter digits only.")