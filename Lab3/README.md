<img width="2205" height="742" alt="image" src="https://github.com/user-attachments/assets/3d38cfab-7f51-470c-83e9-0b92c3500825" />



# create classes 
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
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
lines = file.readlines()
file.close()


# iterate
for x in lines:
    splits = x.split(',') # splits line into individual elements using comma
    shape = splits[0]

    if shape == 'Rectangle':
        rect = Rectangle(int(splits[1]), int(splits[2]))
        print('Area of rectangle is: ', rect.getArea())
    
    elif shape == 'Circle':
        circ = Circle(int(splits[1])) # initialize object as Circle class
        print('Area of circle is: ', circ.getArea()) # calls method
    
    elif shape == 'Triangle':
        tri = Triangle(int(splits[1]), int(splits[2]))
        print('Area of triangle is:', tri.getArea()) 

    else: 
        pass

