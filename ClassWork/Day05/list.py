#!/usr/bin/python

a = [2,3,4,5]

b = list((1,2,3,4, "Hi"))

c = []

print (type(a))
print (type(b))

b.append("GoDzPlaY")
b.insert(1, "RGU5Android")
c.extend(b)

c.extend(b)
c.sort()
d = sorted(b)
d.reverse()
print "Count of a : " +str(d.count("RGU5Android"))


for char in b:
    print (type(char))

print a
print b
print c
print d

