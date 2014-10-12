#!/usr/bin/python

def armstrong_number(number):
    series = []
    value = number
    while value / 10 != 0:
        series.append(value % 10)
        value = value / 10
    series.append(value)
    print(series)
    cubic_value = 0
    for i in series:
        cubic_value += i * i * i
    if cubic_value == number:
        return True
    else:
        return False


if __name__=='__main__':
    number = input("Enter the number: ")
    print("Is the input number an armstrong number : " +str(armstrong_number(number)))
