#!/usr/bin/python

def key_argument(input_string, x, y):
    '''
    In python we can change the order of params in which a function is called.
    This is known as calling the funtion using key-argument means calling the function with the name of the variable=value form the calling function as on line no. 15
    '''
    print("Input_String: " +str(input_string))
    print("X: " +str(x))
    print("Y: " +str(y))


if __name__=='__main__':
    key_argument("Rahul", 10, 50)
    key_argument(x=100, y=500, input_string="GoDzPlaY")
