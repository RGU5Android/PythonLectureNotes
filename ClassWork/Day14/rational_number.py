#!/usr/bin/python

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "Numerator: " +str(self.numerator) + " Denominator: " +str(self.denominator)

    def __add__(self, object):
        print "Add in invoked"
        self.numerator = self.numerator + object.numerator
        self.denominator = self.denominator + object.numerator

    def __sub__(self, object):
        print "Sub in invoked"
        self.numerator = self.numerator - object.numerator
        self.denominator = self.denominator - object.denominator

    def __mul__(self, object):
        print "Mul in invoked"
        self.numerator = self.numerator * object.numerator
        self.denominator = self.denominator * object.denominator

    def __div__(self, object):
        print "Div in invoked"
        self.numerator = self.numerator / object.numerator
        self.denominator = self.denominator / object.denominator


    def __lt__(self, object):
        print "Less-Than in invoked"
        if(self.numerator < object.numerator):
            return True
        else:
            return False

    def __eq__(self, object):
        print "Eqaul in invoked"
        if(self.numerator == object.numerator):
            return True
        else:
            return False

    def __del__(self):
        print "Del is invoked"
        self.numerator = None
        self.denominator = None


r1 = RationalNumber(10,5)
r2 = RationalNumber(20,10)
print r1
print r2

r1 + r2
print r1
print r2

r1 - r2
print r1
print r2

r1 * r2
print r1
print r2

r1 / r2
print r1
print r2
r1.__del__()
r2.__del__()
print r1
print r2


r3 = RationalNumber(10,20)
r4 = RationalNumber(20,40)

if(r3 > r4):
    print "R3 is greater"
else:
    print "R4 is greater"

if(r3 == r4):
    print "R3 & R4 are equal"
else:
    print "R3 & R4 are not equal"

