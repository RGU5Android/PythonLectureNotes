#!/usr/bin/python

import sys

def one():
    print("One")

def two():
    print("Two")

def three():
    print("Three")

def four():
    print("Four")

if __name__=='__main__':
    value = sys.argv[1]
    if(value == "one"):
        one()
    elif(value == "two"):
        two()
    elif(value == "three"):
        three()
    elif(value == "four"):
        four()
    else:
        print("Wrong input to string")

