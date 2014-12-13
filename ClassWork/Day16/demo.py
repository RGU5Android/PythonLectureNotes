#!/usr/bin/python

import math

class PrintVerticallyHorizontally:
    def __init__(self, input_string):
        self.input_string = input_string
        self.length_of_string = len(input_string)
        self.vertical = math.floor(math.sqrt(self.length_of_string))
        self.horizontal = math.ceil(math.sqrt(self.length_of_string))

    def __del__(self):
        self.length_of_string = None
        self.vertical = None
        self.horizontal = None

    def __str__(self):
        return "String: " +str(self.input_string) + " | Length Of String: " +str(self.length_of_string) + " | Vertical: " +str(self.vertical)  +" | Horizontal: " +str(self.vertical)

    def print_pattern(self):
        

if __name__=='__main__':
    one = PrintVerticallyHorizontally("abcdefghijklmnopqrstuvwxyz0123456789")
    print one


