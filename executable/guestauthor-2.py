from author import Author;

"""
Purpose: This file defines guest author class as a subclass of Author
Author: Xiaoyuan Wang
Create date: November 19th, 2024
Last update date: November 19th, 2024
version: 1.0
"""

class GuestAuthor(Author):
    def __init__(self, fn, ln, by, employed_date, articles_contributed=0):
        """
        Initialize the GuestAuthor object with attributes for name, birth year, employment date,
        and articles contributed.
        """
        super().__init__(fn, ln, by)  # Initialize the parent class attributes
        self.employed_date = employed_date  # Employment start date
        self.articles_contributed = articles_contributed  # Number of articles written by the guest author

    def add_article(self):
        """
        Increment the number of articles contributed by the guest author.
        """
        self.articles_contributed += 1

    def get_employment_duration(self, current_year):
        """
        Calculate the duration of employment in years based on the current year.
        """
        if not isinstance(current_year, int):
            raise ValueError("Current year must be an integer.")
        employed_year = int(self.employed_date.split("-")[0])  # Extract year from employed_date
        return current_year - employed_year

    # String representation of GuestAuthor
    def __str__(self):
        return (
            f"{self.firstName} {self.lastName}, born in {self.birthYear}, "
            f"has been employed since {self.employed_date} and has contributed {self.articles_contributed} articles."
        )

