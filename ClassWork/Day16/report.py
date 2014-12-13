#!/usr/bin/python

class Report:
    ID_NUMBER = 1000

    def __init__(self, report_name, report_type):
        print("Report->Constructor")
        Report.ID_NUMBER += 1
        self.__report_id_number = Report.ID_NUMBER
        self.__report_name = report_name
        self.__report_type = report_type

    def __del__(self):
        print("Report->Destructor")
        self.__report_id_number = None
        self.__report_name = None
        self.__report_type = None

    def get_report_information(self):
        return ("Name: " +self.__report_name + " ID: " +str(self.__report_id_number) + " Type: " +self.__report_type)

class ExpenseReport(Report):
    
    def __init__(self, report_name, report_type, total_expense):
        print("ExpenseReport->Constructor")
        Report.__init__(self, report_name, report_type)
        self.__total_expense = total_expense

    def __del__(self):
        print("ExpenseReport->Destructor")
        Report.__del__(self)
        self.__total_expense = None

    def get_report_information(self):
        return Report.get_report_information(self) +" Total Expense: " +str(self.__total_expense)

class ITReport(Report):
    def __init__(self, report_name, report_type, tds, section):
        print("ITReport->Constructor")
        Report.__init__(self, report_name, report_type)
        self.__tds = tds
        self.__section = section

    def __del__(self):
        print("ITReport->Destructor")
        Report.__del__(self)
        self.__tds = None
        self.__section = None

    def get_report_information(self):
        return Report.get_report_information(self) + " TDS: " +str(self.__tds) + " SECTION: " +str(self.__section)


class SalaryReport(Report):
    def __init__(self, report_name, report_type, total_salary):
        print("SalaryReport->Constructor")
        Report.__init__(self, report_name, report_type)
        self.__total_salary = total_salary

    def __del__(self):
        print("SalaryReport->Destructor")
        # Report.__del__(self)
        self.__total_salary = None

    def get_report_information(self):
        return Report.get_report_information(self) + " Total Expense: " +str(self.__total_salary)

if __name__=='__main__':
    expense_report = ExpenseReport("Rahul Uppalwar", "Expense Report", "10000")
    print expense_report.get_report_information()

    it_expense = ITReport("Abhishek Shah", "IT Expense", "1000", "RGU-5")
    print it_expense.get_report_information()

    salary_report = SalaryReport("Zakariya Baduda", "Salary Report", "20000")
    print salary_report.get_report_information()

