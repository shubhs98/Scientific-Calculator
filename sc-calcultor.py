import math

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def squareroot(a):
   result= math.sqrt(a)
   return result
def exp(a):
    return a**2
def sin(a):
    result = math.sin(a)
    return sin
def cos(a):
    result= math.cos(a)
    return result
def tan(a):
    result = math.tan(a)

print("""Choose a operation between 1 to 9
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Square Root
6 - Square
7 - sin
8 - cos
9 - tan"""
      )
num = int(input("Select the operation \n"))

while num<10:
    if num==1:
        print("Enter the parameter")
        a = int(input("Enter your first number \n"))
        b = int(input("Enter your second number \n"))
        print(add(a,b))
    elif num==2:
        print("Enter the parameter")
        a = int(input("Enter your first number \n"))
        b = int(input("Enter your second number \n"))
        print(subtract(a,b))

    elif num==3:
        print("Enter the parameter")
        a = int(input("Enter your first number \n"))
        b = int(input("Enter your second number \n"))
        print(multiply(a,b))

    elif num==4:
        print("Enter the parameter")
        a = int(input("Enter your first number \n"))
        b = int(input("Enter your second number \n"))
        print(divide(a,b))

    elif num==5:
        print("Enter the parameter")
        a = int(input("Enter your  number \n"))

        print(squareroot(a))

    elif num==6:
        print("Enter the parameter")
        a = int(input("Enter your  number \n"))
        print(exp(a))

    elif num==7:
        print("Enter the parameter")
        a = int(input("Enter your  number \n"))

        print(sin(a))

    elif num==8:
         print("Enter the parameter")
         a = int(input("Enter your  number \n"))

         print(tan(a))

    elif num==9:
        print("Enter the parameter")
        a = int(input("Enter your  number \n"))

        print(cos(a))

    else:
        print("Please select another parameter")

    cont = input('Do you want to continue "Yes" or "No \n"')
    if cont=="Yes":
        num = int(input("Enter the parameter \n"))
    else:
        print("Thank You for using this")
        break