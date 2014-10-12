#!/usr/bin/python

def check_number_prime_or_not(input_number):
    for i in range(2, (input_number/2) + 1):
        if (input_number % i) == 0:
            return False
    return True

if __name__=='__main__':
    input_number = input("Enter the number: ")
    print "Is the input number prime: " +str(check_number_prime_or_not(input_number))
