#/usr/bin/python

class Student:
    roll_number = 0

    def __init__(self, name, marks):
        self.roll_number += Student.roll_number
        Student.roll_number += 1
        self.name = name
        self.__marks = marks

    def __str__(self):
        return "Name: " +self.name +" Roll Number: " +str(self.roll_number)  + " Marks: " +self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def calculate_sum(self):
        sum_of_marks = 0
        for i in self.__marks:
            sum_of_marks += i
        return sum_of_marks

if __init__=='__main__':
    rahul = Student("Rahul Uppalwar", [50,60,70])
    print rahul


# setmark, calculate, private marks
