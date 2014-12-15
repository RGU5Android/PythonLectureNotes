#!/usr/bin/python

class AverageRatingException(Exception):
    pass

class PoorRatingException(Exception):
    pass

class GoodRatingException(Exception):
    pass

class InvalidInputException(Exception):
    pass

class IndexOutOfBondException(Exception):
    pass

class Rating(object):
    def __init__(self, rating):
        self.rating = rating

    def print_rating(self):
        if(type(self.rating) == int or type(self.rating) == float):
            if(self.rating < 2):
                raise PoorRatingException
            elif(self.rating >= 2 and self.rating <= 3.5):
                raise AverageRatingException
            elif(self.rating > 5):
                raise IndexOutOfBondException
            else:
                raise GoodRatingException
        else:
            raise InvalidInputException

if __name__=='__main__':
    try:
        r1 = Rating(1)
        r1.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)
    try:
        r2 = Rating(2)
        r2.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)

    try:
        r3 = Rating(3)
        r3.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)

    try:
        r4 = Rating(4)
        r4.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)

    try:
        r5 = Rating(5)
        r5.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)

    try:
        r6 = Rating("Hello")
        r6.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)
 
    try:
        r7 = Rating(7)
        r7.print_rating()
    except Exception as e:
        print str(e.__class__.__name__) +"  " +str(e.message)
 
