#!/usr/bin/python

def userDefinedException(level):
    if level < 1:
        raise Exception("Invalid level : ", level)
    else:
        print ("Entered level is :", level)

def testRaise():
    try:
        level = input("Enter the level: ")
        userDefinedException(level)
    except Exception as e:
        print str(e.__class__.__name__) +"  " + str(e)

if __name__=='__main__':
    testRaise()
