# finding the circumference of a circle using functions
def circumference(a,b):
    return a*b #defining the circumference
x= float(input("Enter the diameter of the circle(radius times by 2):"))#Taking input from user
y = 3.14 #Defining the value of pi

print("The circumference of your circle with a diameter of", x, "is approximately equal to", circumference(x,y))


