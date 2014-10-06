#!/usr/bin/python
import sys

def push(stack_list, input):
    stack_list.append(input)

def pop(stack_array):
    if len(stack_array) == 0:
        return 0
    else:
        value = stack_array.pop()
        return value

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
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print ("Enter the operation to be performed on stack: ")
        print ("1. Print")
        print ("2. Push")
        print ("3. Pop")
        print ("4. Is Empty")
        print ("5. Peep")
        print ("0. Exit")
        try:
            value = int(raw_input("Enter the option: "))
        except (TypeError, NameError, RuntimeError, ValueError):
            value = 6
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        if value == 1:
            print stack_list
        elif value == 2:
            input_value = input("Enter the value to be pushed: ")
            push(stack_list, input_value)
            print ("Now the stack looks like: ")
            print stack_list
            del input_value
        elif value == 3:
            pop_value = pop(stack_list)
            print ("Poped value is : " +str(pop_value))
            print ("Now the stack looks like")
            print stack_list
        elif value == 4:
            print "Stack is empty: " +str(is_empty(stack_list))
        elif value == 5:
            print "Peep value for stack: " +str(peep(stack_list))
        elif value == 0:
            print "Good Byee... :)"
            exit_code()
        else:
            print "Please enter a valid input"

        del value
