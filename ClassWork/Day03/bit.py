#!/usr/bin/python

def toggle_bit_at_position(variable, position):
    if type(variable) is long or type(variable) is int:
        if type(position) is long or type(position) is int:
            position = position - 1 
            value = variable ^ (1 << position)
            return value
        else:
            return "Wrong position value inserted"
    else:
        return "Wrong variable value inserted"

def get_number_of_ones_method_1(variable):
    count = 0
    while(variable):
        if variable & 0x01:
            count += 1
        variable = variable >> 1
    
    return count

def is_number_divisible_by_eight_bit(variable):
    ''' returns True if the number is divisible by 8 else it will return False '''
    if variable & 0x07:
        return False
    else:
        return True

if __name__=='__main__':
    print str(toggle_bit_at_position(12,6))
    print str(get_number_of_ones_method_1(12))
    print str(is_number_divisible_by_eight_bit(12))
