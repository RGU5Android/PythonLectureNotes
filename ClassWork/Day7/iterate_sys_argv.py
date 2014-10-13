#!/usr/bin/python

import sys

def print_sys_argv():
    count = 0
    for input_value in sys.argv:
        print(str(count) +" -> " +str(input_value))
        count += 1

if __name__=='__main__':
    print_sys_argv()
