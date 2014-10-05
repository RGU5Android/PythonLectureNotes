#!/usr/bin/python

def get_tuple_of_number_divisible_by_7():
    list_of_number = []
    for i in range(1000 , 2500):
        if (i % 7 == 0) and (i % 5 <> 0):
            list_of_number.append(i)
    return list_of_number

if __name__=='__main__':
    print ("Number divisible by 7 but not divisible by 5 in range 1000 to 2500 are: ")
    list_of_number = get_tuple_of_number_divisible_by_7()
    print type(list_of_number)
    for i in list_of_number:
        print i

