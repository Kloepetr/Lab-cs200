'''
File Name: student_data.py
Purpose:
This file defines functions used in lab 6
First Create Date: October 3rd, 2024
Last Update Date: October 3rd, 2024
Author: Xiaoyuan Wang
Version: 1.1
'''
def student_information():
    # Create an empty list to store the data of the students.
    students_data = [];

    # A while loop that rerun the user input until user indicates that they are done.
    while True:
        # Get student data using user input
        full_data = input("Enter a student's name, test subject, and grade in percentage (separated by commas): ");
        try:
            # Split the data into name, subject, and grade by commas
            name, subject, grade = full_data.split(',');
            # Make sure grade is stored as a float so decimals are accepted
            grade = float(grade.strip());
            # Ensure that invalid inputs are considered, any number above 100 or below 0 will return invalid.
            if grade < 0 or grade > 100:
                print("Invalid grade. Please enter a value between 0 and 100.");
                continue;
            # Add the student data to the list (name, subject, grade)
            students_data.append([name.strip(), subject.strip(), grade]);
        #if user input anything that isnt formated like x,y,z the code will return a value error.
        except ValueError:
            print("Invalid entry. Make sure to enter name, subject, and grade separated by commas. No need to include '%' sign in percentage grade.");
            continue;

        # Ask the user if they are done after every loop iteration
        stop = input("Are you done? Type 'yes' to finish or press Enter to add another student: ");
        if stop.lower() == 'yes':
            break;

    return students_data;


def grade_convert(gradePercentage):
    # Convert user input grade from percentage to letter grade
    if gradePercentage == 100:
        return 'A+';
    elif gradePercentage >= 90:
        return 'A';
    elif gradePercentage >= 80:
        return 'B';
    elif gradePercentage >= 70:
        return 'C';
    elif gradePercentage >= 60:
        return 'D';
    else:
        return 'F';


def student_data():
    # Get the students' data from student_information
    students = student_information();

    # Initialize second array with a fourth column (letter grades)
    students_with_grades = [];
    #  for loop that calls grade_convert within grade variable in student_information
    for student in students:
        name, subject, grade = student;
        letter_grade = grade_convert(grade);
        #add the converted student letter grade to the list.
        students_with_grades.append([name, subject, grade, letter_grade]);

    # Display first array
    print("\nFirst Array: (Name, Subject, Grade):");
    for student in students:
        print(student);
    # display second array
    print("\nSecond Array: (Name, Subject, Grade, Letter Grade):");
    for student in students_with_grades:
        print(student);
