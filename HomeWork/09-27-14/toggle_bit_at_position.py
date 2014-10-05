#!/usr/bin/python

def toggle_bit_at_position(variable, position):
    if type(variable) is long or type(variable) is int:
        if type(position) is long or type(position) is int:
            position = position - 1 
            value = variable ^ (1 << position)
            return ("Variable: " + str(variable) + " : " + " Position: " + str(position + 1) + " Value after toggle: " + str(value))
        else:
            return "Wrong position value inserted"
    else:
        return "Wrong variable value inserted"

a, b = input("Enter the value for variable and position to be toggled: ")
print (toggle_bit_at_position(a, b));
