"""
#EMPLOYEE_DATA_EXTRATION (header)
File Name: lab5.py
Purpose:
This file calls out the functions imported from the file employee_data;
First Create Date: september 29th , 2024
Last Update Date: October 1st , 2024
Author: Xiaoyuan Wang
Version: 1.1

this is an executable file that aims to store user input of employee information and find the specific employee, display their information, and display the total salary of all employees
project objectives:
1. Create a function for each task, thus your program will have at least two functions. (5’) yes
2. The string contains information of at least five objects. The only hard coded value is the initial
string value, and the value to search for, such as employee name, book title, movie name etc.
The rest must be retrieved through coding. (10’) yes
3. Cannot hard code indexes, e.g. you must use a function or method to retrieve the index of a
semicolon; you must dynamically determine how many employees are in the string. (5’) yes
4. Must have at least one loop structure. (10’) yes
5. Have a utility file and group all the function definitions in this file (10’)yes
6. Program runs successfully, and generates meaningful and correct output (30’)yes
7. Follow professional coding standards (file headers, comments, code blocks, naming conventions,
etc). (10’)yes

"""


#import my user designed functions from my utility file
from employee_data import employee_data;
from employee_data import filter_employee;



employee_list, total_salary = employee_data();  # Get employee data and total salary
filter_employee(employee_list);  # execute filter on inputed employees based on input

# Print total salary, round the final calculated salary to the hundreds.
print(f"Total Salary of All Employees : ${total_salary:.2f}");