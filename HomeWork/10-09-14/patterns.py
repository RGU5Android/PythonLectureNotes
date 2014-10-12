#!/usr/bin/python

def print_pattern_one(line):
    value = ""
    for i in range(line + 1):
        for j in range(i):
            value += (chr(j + 97) + " ")
        value += "\n"
    return value

def print_pattern_two(line):
    value = ""
    for i in range(line + 1):
        for j in range(i):
            value += ("*" + " ")
        value += "\n"
    return value

def print_pattern_three(line):
    value = ""
    for i in range(line + 1):
        for j in range(line + 1 -i):
            value += ("*" + " ")
        value += "\n"
    return value

def print_pattern_four(line):
    value = ""
    for i in range(line + 1):
        for j in range(line + 1 -i):
            value += (" " + "*")
            if j + i == line:
                value += "*"
        value += "\n"
    return value

if __name__ == '__main__':
    line = input("Enter the range for pattern: ")
    print("-------Pattern-------")
    print(print_pattern_one(line))
    print("-------Pattern-------")
    print(print_pattern_two(line))
    print("-------Pattern-------") 
    print(print_pattern_three(line))
    print("-------Pattern-------")
    print(print_pattern_four(line))
