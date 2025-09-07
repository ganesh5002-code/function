# Using functions for the four operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Hello, please pick an operation from below:")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")

choice = input("Enter the letter of your choice from above")
num1 = float(input("Enter your first number"))
num2 = float(input("Enter your second number"))

if choice == "a":
    print("The addition of", num1, "and", num2, "is", add(num1,num2))
elif choice == "b":
    print("The subtraction of", num1, "and", num2, "is", sub(num1,num2))
elif choice == "c":
    print("The multiplication of", num1, "and", num2,"is", multiply(num1,num2))
elif choice == "d":
    print("The division of", num1, "and", num2,"is", divide(num1,num2))
else:
    print("Your choice is invalid")
