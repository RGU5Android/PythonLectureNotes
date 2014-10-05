#!/usr/bin/python

def checkEvenOddNormal(variable) :
	if type(variable) is int or type(variable) is long:
		if variable % 2 == 0 :
			return "Even"
		else :
			return "Odd"
	else :
		print (type(variable))
		return "Number format exception."

def checkEvenOddBitwise(variable) :
    if type(variable) is int or type(variable) is long :
		if variable & 0x01:
			return "Odd"
		else:
			return "Even"

a = input("Enter the number tobe checked for even: ")

print (checkEvenOddNormal(a))

print (checkEvenOddBitwise(a))


