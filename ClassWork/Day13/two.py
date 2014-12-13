#!/usr/bin/python

"""
Write a class point, write constructor, toString method, write a funcation which checks if the two are on same x & y co-ordinate.

Write a class line which will return if the two points intercept
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X-Coordinate: " +str(self.x) + " Y-Coordinate: " +str(self.y)

    def compare(self, object):
        if((self.x == object.x) or (self.y == object.y)):
            return True
        else:
            return False

class Line:
    def __init__(self, startpoint, endpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint

    def __str__(self):
        return "StartPoint: " +str(self.startpoint) + " EndPoint: " +str(self.endpoint)


p1 = Point(10,20)
p2 = Point(15,40)

print p1
print p2

p3 = Point(10,20)
p4 = Point(30,12)
print p3
print p4


l1 = Line(p1,p2)
l2 = Line(p3,p4)

print l1
print l2
