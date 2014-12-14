#!/usr/bin/python
import sys

def return_list_tuple():
    value = str(sys.argv[1])
    print type(value)
    print value
    list_comos = value.split(",")
    tuple_comos = tuple(list_comos)
    print type(list_comos)
    print list_comos
    print type(tuple_comos)
    print tuple_comos

if __name__=='__main__':
    return_list_tuple()
