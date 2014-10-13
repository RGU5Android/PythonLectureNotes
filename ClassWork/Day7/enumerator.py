#!/usr/bin/python

import sys

def print_sys_argv():
    for value in enumerate(sys.argv):
        print type(value)
        print("Index: " +str(value[0]) +" -> " +str(value[1]))
    
    list3 = enumerate(sys.argv)
    print type(list3)
    print list3

if __name__=='__main__':
    print_sys_argv()
