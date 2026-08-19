import math

print("Hello user. Please enter the values.")
x1 = int(input("Please enter x1: "))
y1 = int(input("Please enter y1: "))
x2 = int(input("Please enter x2: "))
y2 = int(input("Please enter y2: "))
#difference:
xdiff = x2 - x1
ydiff = y2 - y1
#exponent:
xsquared = pow(xdiff, 2)
ysquared = pow(ydiff, 2)
#distance and final product:
d = math.sqrt(xsquared + ysquared)
final_product = round(d, 2)
print("The distance between the two points is:",final_product)

#Reflection:
#Using a library is more practical than writing all calculations from scratch because libraries are like a set of tools that can help the the compiler understand what to do.
#Say for example, without using Python's math library, the compiler wouldn't understand what to do for the square root (sqrt() function).
