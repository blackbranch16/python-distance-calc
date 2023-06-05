# Distance Calculator Assignment
print("WElCOME TO THE DISTANCE CALCULATOR!")

# Input 
xOne = float(input("Enter value of x1: "))
yOne = float(input("Enter value of y1: "))
xTwo = float(input("Enter value of x2: "))
yTwo = float(input("Enter value of y2: "))

# Process
import math
result = math.sqrt(((xTwo - xOne) ** 2) + ((yTwo - yOne) ** 2))

# Output
print("Distance betweeen the two points is " + str(result) + ".")