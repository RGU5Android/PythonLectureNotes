#!/usr/bin/python

def variable_number_of_args(default, *args, **argws):
    
    ''' 
    Input params to this function is a default argument
    then a tuple which is a immutable, hetrogenious array
    then a dist which can store values in <key,value> format
    '''

    print type(args)
    print type(argws)
    print("Default: " +str(default))
    
    print("Printing Dist: ")
    for data in argws:
        print(data, argws[data])

    print("Printing Types ")
    i = 0
    for arg in args:
        i += 1
        print("arg:" +str(i) +" ->" +str(arg))

if __name__=='__main__':

    variable_number_of_args(1,2,3,1,3,4,3,4,5,4,3,2,4,5,"asdfasdf", "asfdasdf", name="Rahul", age=28)
