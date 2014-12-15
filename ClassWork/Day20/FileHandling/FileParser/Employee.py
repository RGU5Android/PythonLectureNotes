#!/usr/bin/python

class Employee(object):
    def __init__(self, emp_id, emp_name, emp_salary, emp_designation):
        self.emp_designation = emp_designation
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def __str__(self):
        return "Employe Name: " +self.emp_name +"Employe ID: " +self.emp_id
