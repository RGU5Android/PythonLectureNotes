#!/usr/bin/python

def get_number_of_zeros_or_ones(variable , character):
    ''' returns the number of zeros or ones in the binary of the variable using a for loop '''
    string_number = bin(variable)
    string_number = string_number.replace("0b", "")
    i = 0
    for character_in_str in string_number:
        if character_in_str == str(character):
            i += 1
    return i

def get_number_of_zeros_or_ones_builtin(variable , character):
    ''' returns the number of zeros or ones in the binary of the variable using count function'''
    string_number = bin(variable)
    string_number = string_number.replace("0b", "")
    return string_number.count(str(character))

def get_number_of_ones_method_1(variable):
    count = 0
    while(variable):
        if number & 0x01:
            count += 1
        number = number >> 1
    return count

def get_number_of_ones_method_2(variable):
    count = 0
    while(variable):
        number = (number) & (number - 1)
        count += 1
    return count

variable = input("Enter a integer value: ")
character = input("What you want to count -> 0 or 1: ")


print ("Number of " + str(character) + " in " + str(variable) + "\nwhose binary value is : " + str(bin(variable)) + "\nis: " + str(get_number_of_zeros_or_ones(variable, character)))
print ("---------------------------------------------------------------------------------------------------")
print ("Number of " + str(character) + " in " + str(variable) + "\nwhose binary value is : " + str(bin(variable)) + "\nis: " + str(get_number_of_zeros_or_ones_builtin(variable, character)))
print ("---------------------------------------------------------------------------------------------------")

print str(get_number_of_ones_method_1(variable))
print str(get_number_of_ones_method_2(variable))
