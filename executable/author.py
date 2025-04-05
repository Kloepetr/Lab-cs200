"""
File name: author.py
Purpose: This file defines author class
Author: Xiaoyuan Wang
Create date: November 11th 2024
Last update date: November 12th, 2024
version: 1.1
"""
class Author:
    def __init__(self, fn, ln, by):
        # make sure input is an integer
        if not isinstance(by, int):
            raise ValueError("Birth year must be an integer.");
        self.firstName = fn;
        self.lastName = ln;
        self.birthYear = by;
    # Method to calculate age based on current year
    def get_age(self, current_year):
        #make sure input is an integer
        if not isinstance(current_year, int):
            raise ValueError("Current year must be an integer.");
        return current_year - self.birthYear;

    # String representation of the Author
    def __str__(self):
        return f"{self.firstName} {self.lastName} was born in {self.birthYear}.";


