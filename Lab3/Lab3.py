# Hannah Diaz
# GEOG 676 GIS Programming
# Spring 2026
# 8 February 2026

# Lab 3 - Object Oriented Programming, Shapes 


# create classes 
class Shape(): # creates parent class; kind of unnecessary here
    def __init__(self):
        pass

class Rectangle(Shape): # child classes
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height



# read shape.txt file 
file = open('C:\\GEOG676\\M4\\shape.txt', 'r')
lines = file.readlines() # returns multiple lines/ each line has multiple values
file.close()


# iterate
for x in lines:
    splits = x.split(',') # splits line into individual elements using comma
    shape = splits[0] # index 0 is name of shape

    if shape == 'Rectangle':
        rect = Rectangle(int(splits[1]), int(splits[2])) # initialize object as Rectangle class; index
        print('Area of rectangle is: ', rect.getArea()) # calls getArea method from Rectangle class
    
    elif shape == 'Circle':
        circ = Circle(int(splits[1])) # initialize object as Circle class
        print('Area of circle is: ', circ.getArea()) # calls method
    
    elif shape == 'Triangle':
        tri = Triangle(int(splits[1]), int(splits[2]))
        print('Area of triangle is:', tri.getArea()) 

    else: 
        pass


# # failed attempt at class iteration below 
# class Rectangle:

#     def __init__(self): 
#         pass

#     # def __init__(self, l, w):
#     #     self.len = l
#     #     self.wid = w

#     def __iter__(self):
#         self.i = 1

#     def __next__(self):
#         splits = i.split(',')
#         shape = splits[0]

#         if self.i > len(lines) or shape != 'Rectangle':
#             raise StopIteration
        
#         len = int(splits[1])
#         wid = int(splits[2])

#         recArea = len * wid
#         return int(recArea)


# for x in Rectangle(len(lines)):
#     print(x)











