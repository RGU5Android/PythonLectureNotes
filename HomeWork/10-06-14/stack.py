#!/usr/bin/python
import sys

def push(stack_list, input):
    stack_list.append(input)
    return stack_list

def pop(stack_array):
    if len(stack_array) == 0:
        return 0, stack_array
    else:
        value = stack_array.pop()
        return value, stack_array

def peep(stack_array):
    value = len(stack_array)
    if value == 0:
        return 0
    else:
        return stack_array[value -1]

def is_empty(stack_array):
    if len(stack_array) == 0:
        return True
    else:
        return False

def exit_code():
    sys.exit()

if __name__=="__main__":
    stack_list = []
    while True:
        value = 0
        print ("Enter the operation to be performed on stack: ")
        print ("1. Print")
        print ("2. Push")
        print ("3. Pop")
        print ("4. Is Empty")
        print ("5. Peep")
        value = eval(raw_input("Enter the option: "))

        if value == 1:
            print stack_list
        elif value == 2:
            input_value = input("Enter the value to be pushed: ")
            stack_list = push(stack_list, input_value)
            print ("Now the stack looks like: ")
            print stack_list
            del input_value
        elif value == 3:
            pop_value, stack_list = pop(stack_list)
            print ("Poped value is : " +str(pop_value))
            print ("Now the stack looks like")
            print stack_list
        elif value == 4:
            print "Stack is empty: " +str(is_empty(stack_list))
        elif value == 5:
            print "Peep value for stack: " +str(peep(stack_list))
        else:
            exit_code()

        del value
