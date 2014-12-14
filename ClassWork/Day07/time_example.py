#!/usr/bin/python

variable = 0

def change_value():
    #global variable
    print id(variable)
    variable += 1
    print id(variable)

if __name__=="__main__":
    change_value()
