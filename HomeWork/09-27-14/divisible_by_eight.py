#!/usr/bin/python

def is_number_divisible_by_eight(variable):
    ''' returns True if the number is divisible by 8 else it will return False '''
    string_number = bin(variable)
    string_number = string_number.replace("0b", "")
    return string_number.endswith("000")

def is_number_divisible_by_eight_bit(variable):
    ''' returns True if the number is divisible by 8 else it will return False '''
    if variable <> 0:
        if variable & 0x07:
            return False
        else:
            return True
    else:
        return False
variable = input("Enter the number that needs to be evaluated: ")
if type(variable) is int or type(variable) is long:
    print("Is " + str(variable) + " divisible by 8 : " + str(is_number_divisible_by_eight(variable)))
    print("Is " + str(variable) + " divisible by 8 : " + str(is_number_divisible_by_eight_bit(variable)))

else:
    print("Invalid input")
