# # Inputs for triangle
# s1 = float(input("Enter the first side of the triangle: "))
# s2 = float(input("Enter the second side of the triangle: "))
# s3 = float(input("Enter the third side of the triangle: "))

# # Perimeter and area calculation for triangle
# p = s1 + s2 + s3
# s = p / 2
# area_triangle = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

# # Print perimeter and area of the triangle
# print("The perimeter of the triangle is: {0:.2f}".format(p))
# print("The area of the triangle is: {0:.2f}".format(area_triangle))

# # Input for circle
# PI = 3.14
# r = float(input("Enter the radius of a circle: "))

# # Area and perimeter calculation for circle
# area_circle = PI * r * r
# perimeter_circle = 2 * PI * r

# # Print area and perimeter of the circle
# print("Area of the circle: %.2f" % area_circle)
# print("Perimeter of the circle: %.2f" % perimeter_circle)

# import cmath

# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# d = (b**2) - (4*a*c)

# sol1 = (-b - cmath.sqrt(d)) / (2*a)
# sol2 = (-b + cmath.sqrt(d)) / (2*a)

# print('The solutions are {0} and {1}'.format(sol1, sol2))

# # Python Program to Swap Two Variables
# P = int(input("Please enter value for P: "))
# Q = int(input("Please enter value for Q: "))

# # Swap the values
# temp = P
# P = Q
# Q = temp

# # Print the swapped values
# print("The Value of P after swapping: ", P)
# print("The Value of Q after swapping: ", Q)

# # Python Program to Convert Kilometres to Miles
# km = float(input("Enter value in kilometers: "))

# # Note: 1 km = 0.621371 miles
# conv_fac = 0.621371
# miles = km * conv_fac

# print("%0.2f kilometers is equal to %0.2f miles" % (km, miles))

# # Python Program to Convert Celsius to Fahrenheit
# Celsius = float(input("Enter Celsius temperature: "))
# Fahrenheit = (Celsius * 1.8) + 32
# print("%0.1f degree Celsius is equal to %0.1f degree Fahrenheit" % (Celsius, Fahrenheit))