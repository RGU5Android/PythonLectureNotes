#!/usr/bin/python

import math 

def is_square(x):
    a = int(math.sqrt(x)) * int(math.sqrt(x))
    if(a == x):
        return True
    else:
        return False

# map keyword
list1 = map(lambda x:x*x, [1,2,3,4,5,6,7,8,9])
print list1

# filter keyword
list2 = filter(lambda x: (x%2 == 0) & (x%4 != 0), [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1])
print list2

# reduce keyword
list3 = reduce(lambda x,y:x+y, [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1])
print list3

# filter keyword
list4 = map(lambda x: (x%2 == 0) & (x%4 != 0), [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1])
print list4

# similar to inline ananomius function
# add = lambda x,y: x+y

# list comprihension:- 
print [x for x in range(100) if ((x%10 == 0) & (x%20 != 0))]
print [x for x in range(100) if(is_square(x))]

