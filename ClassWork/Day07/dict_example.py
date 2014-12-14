#!/usr/bin/python

def print_dict():
    dict_value = {"Name":"Rahul", "Middle Name":"Gunvant", "Surname":"Uppalwar"}
    print type(dict_value)
    dict_value["DOB"] = "05-05-1988"
    dict_value.update({"Name":"RGU5Android"})
    for key in dict_value.keys():
        print "Key: " +str(key +" has value " +str(dict_value.get(key)))


if __name__=='__main__':
    print_dict()
