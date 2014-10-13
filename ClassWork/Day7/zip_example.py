#!/usr/bin/python

def print_key_value_zip():
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = ["rgu", "asdf", "asdf", "asdfasdfasdf", "asdfasqweqwe"]
    for i in zip(list1,list2):
        print type(i)
        print i

    list3 = zip(list1, list2)
    print type(list3)
    print list3

if __name__=='__main__':
    print_key_value_zip()
