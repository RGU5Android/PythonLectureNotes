#!/usr/bin/python

def add(value1, value2):
    return (value1 + value2)

def sub(value1, value2):
    return (value1 - value2)

def mul(value1, value2):
    return (value1 * value2)

def div(value1, value2):
    return (value1 / value2)

value1, value2 = input("Enter two numbers: ")

if __name__=='__main__':
    print ("Add : " + str(add(value1, value2)))
    print ("Sub : " + str(sub(value1, value2)))
    print ("Mul : " + str(mul(value1, value2)))
    print ("Div : " + str(div(value1, value2)))
