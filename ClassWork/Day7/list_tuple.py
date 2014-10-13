#!/usr/bin/python

def return_list_tuple(input_string):
    value = str(input_string)
    print type(value)
    print value
    list_comos = value.split(",")
    tuple_comos = tuple(list_comos)
    print type(list_comos)
    print list_comos
    print type(tuple_comos)
    print tuple_comos

if __name__=='__main__':
    input_string = raw_input("Enter the string seperated by comas: ")
    return_list_tuple(input_string)
