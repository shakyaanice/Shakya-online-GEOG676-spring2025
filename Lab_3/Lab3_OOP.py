import math

# Define shape classes
class Shape():
    def __init__(self):
        pass

# Create shape objects
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

#Read data from the text file
with open(r'C:\Users\shaky\OneDrive - Texas A&M University\Documents\GitHub\Shakya-online-GEOG676-spring2025\Lab_3\shape.txt', 'r') as file:
    lines = file.readlines()

#Parse data for iteration and print area
for line in lines:
    components = line.split(',')
    shape=components[0]

    if shape == "Rectangle":
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of Rectangle is:', rect.area())
    elif shape == "Circle":
        cir = Circle(int(components[1]))
        print('Area of Circle is:', cir.area())
    elif shape == "Triangle":
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of Triangle is:', tri.area())
    else:
        pass

 