#!/usr/bin/python

try:
    fd = open("aaa","r")
    fd.write("Hello World!!!!")
except (IOError, Exception) as e:
    print e
else:
    print "Else block of exception"
finally:
    fd.close()

#try:
#    print a
#except Exception as e:
#    print e

#try:
#    name = "Rahul"
#    age = 25
#    result = name + age
#except Exception as x:
#    print type(x)
#    print x.__class__.__name__
#    print x.message
