#!/usr/bin/python

class Report:
    ID_NUMBER = 1000

    def __init__(self, report_name, report_type):
        Report.ID_NUMBER += 1
        self.__report_id_number = Report.ID_NUMBER
        self.__report_name = report_name
        self.__report_type = report_type

    def __del__(self):
        self.__report_id_number = None
        self.__report_name = None
        self.__report_type = None

    def get_report_information(self):
        return ("Name: " +self.__report_name + " ID: " +str(self.__report_id_number) + " Type: " +self.__report_type)

class ExpenseReport(Report):
    
    def __init__(self, report_name, report_type, total_expense):
        Report.__init__(self, report_name, report_type)
        self.__total_expense = total_expense

    def __del__(self):
        Report.__del__(self)
        self.__total_expense = None

    def get_report_information(self):
        return Report.get_report_information(self) +" Total Expense: " +str(self.__total_expense)

class ITReport(Report):
    def __init__(self, report_name, report_type, tds, section):
        Report.__init__(self, report_name, report_type)
        self.__tds = tds
        self.__section = section

    def __del__(self):
        Report.__del__(self)
        self.__tds = None
        self.__section = None

    def get_report_information(self):
        return Report.get_report_information(self) + " TDS: " +str(self.__tds) + " SECTION: " +str(self.__section)


class SalaryReport(Report):
    def __init__(self, report_name, report_type, total_salary):
        Report.__init__(self, report_name, report_type)
        self.__total_salary = total_salary

    def __del__(self):
        Report.__del__(self)
        self.__total_salary = None

    def get_report_information(self):
        return Report.get_report_information(self) + " Total Expense: " +str(self.__total_salary)

