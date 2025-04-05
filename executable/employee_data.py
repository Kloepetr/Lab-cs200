"""
#EMPLOYEE_DATA_STORAGE_AND_FILTER (header)
File Name: employee_data.py
Purpose:
This file defines the functions employee_data and a function that filters employee_data which will be imported to my lab 5;
First Create Date: september 29th , 2024
Last Update Date: October 1st , 2024
Author: Xiaoyuan Wang
Version: 1.1
"""


def employee_data():
    #create a local variable that asks the user how many employee is in their company, this will determine the amount of for loops to run
    employee_number = int(input("How many employees are you trying to filter? "));
    #store the employee information in a list
    employees = [];
    #this is the initial amount of salary when 0 employees are inputed. It will be updated when user input is stored
    total_salary = 0.0;
    #the for loop is ran, where the parameter is the integer user input determining how many
    for i in range(employee_number):
        full_data = input("Please enter your employee's data in the format (full name, age, zodiac sign, position, salary) separated by commas, do not enter a comma after salary. ");

        #Get the first occurance of a comma, this is where user store the employee's name
        first_comma_index = full_data.find(',');
        #Get the last occurance of a comma, this is where user store the employee's salary
        last_comma_index = full_data.rfind(',');
        # If the first and last comma indices are the same, meaning there is one comma in the string, there is no employee age, zodiac sign, or position
        if first_comma_index == last_comma_index:
            #the employee's name is the found before the first comma of the string of the user input
            employee_name = full_data[:first_comma_index].strip();
            #convert the employee salary a float
            employee_salary = float(full_data[last_comma_index + 1:].strip());
            employee_info = ""  # The display is blank, which means if the string user inputed only has one comma, then there is no information in the middle which has the employee's age, zodiac sign, and position
        else:
            #the employee's name is the found before the first comma of the string of the user input
            employee_name = full_data[:first_comma_index].strip();
            #the employee's salary is the found after the last comma of the string of the user input
            employee_salary = float(full_data[last_comma_index + 1:].strip());  # Convert salary to float
            #Slice out everything in between first and last comma  for employee's age, zodiac sign, and position
            employee_info_string = full_data[first_comma_index + 1:last_comma_index].strip();
            #store employee's information in a list
            employee_info = [];
            # Continue to run the code until there are no more information displayed in between the first comma and the last comma, which has the employee's age, zodiac sign, and position
            while employee_info_string:
                # define the variable next_comma_index to find the next comma
                next_comma_index = employee_info_string.find(',');
                if next_comma_index == -1:  # if no more commas are found
                    employee_info.append(employee_info_string);  #end loop
                    break;
                else:
                    # Append the part before the next comma to employee info
                    employee_info.append(employee_info_string[:next_comma_index].strip());
                    # Slice out the substring from the index to the end
                    # Update the string
                    employee_info_string = employee_info_string[next_comma_index + 1:];

        # Store employee details as a tuple in the list
        employees.append((employee_name, employee_info, employee_salary));
        #calculate the total salary
        total_salary += employee_salary;
 # Return all employee data and total salary
    return employees, total_salary;


def filter_employee(employees):
    #ask user which employee they are looking for
    name_search = input("Who are you trying to look for? ").strip();

    # Iterate through the employee list to find the employee
    #check if employee is found
    found = False;
    #find the employee in the list of employees
    for employee in employees:
        # Extract the employee name for comparison
        employee_name = employee[0];
        # make user input case sensitive
        if name_search.lower() == employee_name.lower():
            #the employee's name is the 0th in the list, I used the join command to join my information into a string separated by a comma if there are information after the employee's name. If not, my function will return "none". afterwards, the function will list out the third item as employee [2], which is the salary.
            print(f"Employee Name: {employee[0]}, Employee Info: {', '.join(employee[1]) if employee[1] else 'None'}, Employee Salary: {employee[2]}") #this is extracted from the list {employee_name, employee_info, employee_salary}
            found = True;
            break;  # Stop searching after the first match
    #
    if not found: #if third user input (specific name search) does not match any of the second user input (employee datas), tell them that the employee cannot be found.
        print("Employee not found.");

