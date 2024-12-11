import math
type=input("Enter your shape =")
class shape:
    """
this class is used to get the area and the circumference of the shapes
--------------
parameters

enter the shape type
if the type == rectangle
enter the width
enter the heigh
------
if the type == circle
enter the radius
pi=3.14
------
if the type == triangle
enter the base
enter the first distribution
enter the second distribution
-------
----------------
retern
retern the area and the circumference of the shape you entered 
if the type == rectangle
retern area and circumference
--------
if the type == circle
retern area and circumference
-------
if the type == triangle
retern area and circumference
    """
    def __init__(self,type):
        pass
    def see(self):
        if type=="rectangle": 
            width=int(input("Enter the width ="))
            heigh=int(input("Enter the heigh ="))
            self.rectangle(width,heigh)
        elif type=="circle":
            radius=float(input("Enter the radius ="))
            self.circle(radius)
        elif type=="triangle":
            base=int(input("Enter the base ="))
            first_district=int(input("Enter the first district ="))
            second_district=int(input("Enter the second district ="))
            self.triangle(base,first_district,second_district)
        else:
            print("this is not the shape")
    def rectangle(self,width,heigh):
                area=width*heigh
                circumference=(width+heigh)*2
                print(area)
                print(circumference)
    def circle(self,radius,pi=3.14):
                area=pi*radius**2
                circumference=2*pi*radius
                print(area)
                print(circumference)
    def triangle(self,base,first_district,second_district):
                circumference=base+first_district+second_district
                half_circumference=circumference/2
                area=math.sqrt(half_circumference*(half_circumference-base)*(half_circumference-first_district)*(half_circumference*second_district))
                print(area)
                print(circumference)
emp=shape(type)
emp.see()