#!/usr/bin/python
"""
OOPs
*   Polymorphysim:  One interface multiple defination.
                    Only RUN-TIME Polymorphism is supported.

    Inheritence:    - "IS A Relationship"
                    - "HAS A Relationship"

Write a class of Complex Number in Python
"""

class ComplexNumber:
    """
    SELF - this
    """
    name = "Rahul"

    def __init__(self, real, imaginary):
        '''
        Every variable associated with self is class level feild.
        '''
        self.iReal = real
        self.iImaginary = imaginary

    def display(self):
        print self.iReal
        print self.iImaginary

    def add(self, c2):
        return ComplexNumber(self.iReal + c2.iReal, self.iImaginary + c2.iImaginary)
        # self.iReal = self.iReal + c2.iReal
        # self.iImaginary = self.iImaginary + c2.iImaginary

    def __str__(self):
        return "Real: " +str(self.iReal) +" Imaginary: " +str(self.iImaginary)

c1 = ComplexNumber(10, 20)
# c1.display()
# print c1.iReal
# print c1.iImaginary
# c1.iReal = 1000;
# print c1.iReal
c2 = ComplexNumber(100, 200)
c3 = c1.add(c2)
# c3.display()
# print id(c3.name)
# print id(c1.name)
# print ComplexNumber.name
c3.xyz = 10
# print c3.__dict__
print c1
print c2
print c3

#print ComplexNumber.__dict__
