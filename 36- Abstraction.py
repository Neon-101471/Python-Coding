print(" ")
from abc import ABC, abstractclassmethod
class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractclassmethod
    def area (self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("The area of Triangle is = ", area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("The area of Rectangle is = ", area)

triangle = Triangle(10, 20)
triangle.area()
rectangle = Rectangle(10, 12)
rectangle.area()