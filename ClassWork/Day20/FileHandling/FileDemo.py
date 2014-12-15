#!/usr/bin/python

# WAP to open a file in read mode and find out what all attributes are associated with fd.
# Read all the lines of file & display them.

import os

class ReadFile(object):
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        pass


if __name__=='__main__':
    file_name = raw_input("Enter the filename: ")
    if (os.path.isfile(file_name)):
        try:
            fd = open(file_name, 'r')
            print fd.readlines()
            os.chmod(file_name, 700)
        except Exception as e:
            print e
        finally:
            fd.close()
    else:
        print "File not present"
    


