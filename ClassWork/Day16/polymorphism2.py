#!/usr/bin/python
import math

class Shape:
    def __init__(self):
        print("Shape Constructor is invoked")

    def __del__(self):
        print("Shape Distructor is invoked")

    def calculate_area(self):
        pass

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return (self.radius * math.pi * 3.14)

    def draw(self):
        print("Draw method for Circle")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return (self.length * self.length)

    def draw(self):
        print("Draw method for Square")


class Rectangle(Shape):
    def __init__(self, length, breathe):
        self.length = length
        self.breathe = breathe

    def calculate_area(self):
        return (self.length * self.breathe)

    def draw(self):
        print("Draw method for Rectangle")

class TestShape:
    def draw(self, shape):
        shape.draw()

    def area(self, shape):
        print("Area for this shape of type " +str(type(shape)) +" is " +str(shape.calculate_area()))



if __name__=='__main__':
    circle = Circle(10)
    square = Square(20)
    rectangle = Rectangle(10,20)
    testshape = TestShape()

    testshape.draw(circle)
    testshape.draw(square)
    testshape.draw(rectangle)

    testshape.area(circle)
    testshape.area(square)
    testshape.area(rectangle)
