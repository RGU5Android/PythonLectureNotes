#!/usr/bin/python

def fibonacci_series(number):
    number1 = 0
    number2 = 1
    series = [0,1]
    for i in range(number):
        fibo_number = number1 + number2
        series.append(fibo_number)
        number1 = number2
        number2 = fibo_number
    return series

if __name__=='__main__':
    number = input("Enter the max range for fibonacci series: ")
    print("The series is : " +str(fibonacci_series(number)))
