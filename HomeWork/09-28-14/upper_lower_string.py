#!/usr/bin/python

def convert_to_upper(string):
    ''' returns string converting it into upper case'''
    return str.upper(string)
f1 = convert_to_upper

def convert_to_upper(string , y=10):
    return str.upper(string + str(y))
f2 = convert_to_upper

def convert_to_lower(string):
    ''' returns string converting it into lower case'''
    return str.lower(string)

if __name__=='__main__':
    string = raw_input("Enter the string: ");
    print("String in upper case: " + convert_to_upper(string))
    print("String in lower case: " + convert_to_lower(string))
    print(f1(string))
    print(f2(string))
