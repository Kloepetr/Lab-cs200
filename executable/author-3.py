"""
File name: author.py
Purpose: This file serves as parent class for the child class guestAuthor
Author: Xiaoyuan Wang
Create date: November 19th 2024
Last update date:November 19th 2024
version: 1.1
"""
class Author:
    def __init__(self, first_name, last_name, birth_year):
        if not isinstance(birth_year, int):
            raise ValueError("Birth year must be an integer.")
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_age(self, current_year):
        if not isinstance(current_year, int):
            raise ValueError("Current year must be an integer.")
        return current_year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, born in {self.birth_year}."

    # Setter and getter decorators
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first_name = value
