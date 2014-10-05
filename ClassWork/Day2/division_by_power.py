#!/usr/bin/python

def multiplyByPowerOf2Bitwise(variable , power):
	if (type(variable) is int or type(variable) is long) and (type(power) is int or type(power) is long):
		return variable >> power
	else:
		return "Invalid input"
a , b = input("Enter number & power: ")
print (multiplyByPowerOf2Bitwise(a , b))
