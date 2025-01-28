#Read data from the text file
with open(r'C:\Users\shaky\OneDrive - Texas A&M University\Documents\GitHub\Shakya-online-GEOG676-spring2025\Lab_3\shape.txt', 'r') as file:
    shapes_data = file.readlines()

#Parse data for iteration later in process
shapes = []
for line in shapes_data:
    parts = line.strip().split(",")
    shape_name = parts[0]
    dimensions = list(map(float, parts[1:]))  # Convert dimensions to float
    shapes.append((shape_name, dimensions))

import math

# Define shape classes
class Shape():
    def area(self):
        pass

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

# Create shape objects
shape_objects = []
for shape_name, dimensions in shapes:
    if shape_name == "Rectangle":
        shape = Rectangle(*dimensions)  # Unpack dimensions as arguments for __init__ method of each class
    elif shape_name == "Circle":
        shape = Circle(*dimensions)
    elif shape_name == "Triangle":
        shape = Triangle(*dimensions)
    shape_objects.append(shape)

# Print shape areas
for shape in shape_objects:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")

 