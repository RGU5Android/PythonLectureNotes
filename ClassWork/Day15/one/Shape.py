#!/usr/bin/python

class Shape:
    class_attribute = 1000
    def __init__(self, length):
        self.attribute = 100
        print("Constructor of Shape class is invoked " +str(length))

    def __del__(self):
        print("Destructor of Shape class is invoked ")

    def draw(self):
        pass

class Square(Shape):
    def __init__(self, length):
        #super(Square,self).__init__(length) // this works with python 3.4
        Shape.__init__(self, length) # this wors with python 2.7
        self.length = length
        print ("Constructor of Square class is invoked " +str(length))

    def __del__(self):
        print ("Destructor of Square class is invoked ")

    def draw(self):
        print ("Draw method of Square is invoked ")

class Circle(Shape):
    def __init__(self, length):
        #super(Square,self).__init__(length) // this works with python 3.4
        # Shape.__init__(self, length) # this wors with python 2.7
        self.length = length
        print ("Constructor of Circle class is invoked " +str(length))

    def __del__(self):
        print ("Destructor of Circle class is invoked ")

    def draw(self):
        print ("Draw method of Circle is invoked ")

class Rectangle(Shape):
    def __init__(self, length):
        
        #super(Square,self).__init__(length) // this works with python 3.4
        Shape.__init__(self, length) # this wors with python 2.7
        self.length = length
        print ("Constructor of Rectangle class is invoked " +str(length))

    def __del__(self):
        print ("Destructor of Rectangle class is invoked ")

    def draw(self):
        print ("Draw method of Rectangle is invoked ")

class TestShape:
    def __init__(self):
        print("TestShape Constructor is invoked")

    def __del__(self):
        print("TestShape Destructor is invoked")

    def print_draw(self, shape):
        print shape.__dict__
        shape.draw()

        
sq = Square(10)
# sq.draw()
# sq2 = Square(20)
# sq2.draw()
# sq3 = Square(30)
# sq3.draw()

cr = Circle(40)
# cr.draw()
# cr1 = Circle(50)
# cr1.draw()
# cr2 = Circle(60)
# cr2.draw()

rt = Rectangle(70)
#rt.draw()
#rt1 = Rectangle(80)
#rt1.draw()
#rt2 = Rectangle(90)
#rt2.draw()
#print id(rt2.class_attribute)
#print id(rt1.class_attribute)

test_shape = TestShape()
test_shape.print_draw(sq)
test_shape.print_draw(cr)
test_shape.print_draw(rt)
