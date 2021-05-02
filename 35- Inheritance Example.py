print(" ")
class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area (self):
        print("This is shape template.")
    #If you don't write this function, definitely program will be run under Triangle & Rectangle class.

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