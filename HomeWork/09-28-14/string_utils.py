#!/usr/bin/python

def get_number_of_vovels(input_string):
    input_string = str.lower(input_string)
    count = 0
    for char in input_string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    return count

def get_number_of_blank_spaces(input_string):
    count = 0
    for char in input_string:
        if str.isspace(char):
            count += 1
    return count

def get_number_of_special_character(input_string):
    count = 0
    for char in input_string:
        if not (str.isalpha(char) or str.isdigit(char) or str.isspace(char)):
            count += 1
    return count

def get_number_of_digits(input_string):
    count = 0
    for char in input_string:
        if str.isdigit(char):
            count += 1
    return count

def get_count_vovel_blank_spaces_special_char_digits(input_string):
    vovel_count = 0
    special_char_count = 0
    space_count = 0
    digit_count = 0

    #for ch in input_string:
    for i in range(len(input_string)):
        ch = input_string[i]
        if ch.isspace():
            space_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch.isalpha() and ch.lower() in "aeiou":
            vovel_count += 1
        elif not ch.isalpha():
            special_char_count += 1
    return vovel_count, special_char_count, space_count, digit_count


if __name__=='__main__':
    input_string = raw_input("Enter the string to be examined: ")
    print("String contains " + str(get_number_of_vovels(input_string)) + " vovels")
    print("String contains " + str(get_number_of_blank_spaces(input_string)) + " blank spaces")
    print("String contains " + str(get_number_of_digits(input_string)) + " digits")
    print("String contains " + str(get_number_of_special_character(input_string)) + " special character")
    vovel_count, special_char_count, space_count, digit_count = get_count_vovel_blank_spaces_special_char_digits(input_string)
    print("String contains \nVovels: " +str(vovel_count) +" Special Char: " +str(special_char_count) +" Space count: " +str(space_count) +" Digit Count: " +str(digit_count))
    print("String contains \nVovels: {} Special Char: {} Space count: {} Digit Count: {}".format(vovel_count, special_char_count, space_count, digit_count))

