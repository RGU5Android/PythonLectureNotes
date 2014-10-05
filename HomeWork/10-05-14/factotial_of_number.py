#!/usr/bin/python
import math

def get_factorial_of_number(input_number):
    value = 1
    for i in range(1, input_number+1):
        value *= i
    return value

def get_factorial_of_number_predefined(input_number):
    return math.factorial(input_number)


if __name__=='__main__':
    number = input("Enter the value: ")
    print("Factorial of : " +str(number) +" is: " +str(get_factorial_of_number(number)))
    print("Factorial of : " +str(number) +" is: " +str(get_factorial_of_number_predefined(number)))
