# Name: Minhyuk KIm 
# Email: minhyuk.kim@stonybrook.edu
# SBUID: 115944468

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    celsius = float(5/9*(fahrenheit - 32))
    print("The temperature is " + '{:.2f}'.format(celsius) + " Celsius")
    return celsius

def what_to_wear(celsius):
    if (celsius<-10):
       print("Wear Puffy jacket")
    elif (-10<=celsius<0):
        print("Wear Scarf")
    elif (0<=celsius<10):
        print("Wear Sweater")
    elif (10<=celsius<=20):
        print("Wear Light jacket")
    elif (20<celsius):
        print("Wear T-shirt")
        

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(((x1*y2 + x2*y3 + x3*y1)-(x1*y3 + x2*y1 + x3*y2))/2)

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    a = euclidean_distance(x1, y1, x2, y2)
    b = euclidean_distance(x2, y2, x3, y3)
    c = euclidean_distance(x3, y3, x1, y1)
    return a + b + c


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 
import math

def deg2rad(deg):
    return (deg)*math.pi/180

def apothem(number_sides, length_side):
   n = number_sides
   s = length_side
   a = s/(math.tan(deg2rad(180/n))*2)
   return a

def polygon_area(number_sides, length_side):
   n = number_sides
   s = length_side
   return (n*s*apothem(number_sides, length_side))/2
 

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

