"""
File name: website.py
Purpose: This file defines the website class
Author: Xiaoyuan Wang
Create date: November 11th 2024
Last update date:November 12th 2024
version: 1.1
"""
class Website:
    def __init__(self, title, location, year_established):
        self.title = title;
        self.location = location;
        self.yearEstablished = year_established;

    # Setter for title
    def set_title(self, title):
        if isinstance(title, str):
            self.title = title;
        else:
            raise ValueError("Title must be a string.");

    # Setter for location
    def set_location(self, location):
        if isinstance(location, str):
            self.location = location;
        else:
            raise ValueError("Location must be a string.");

    # Setter for year established
    def set_year_established(self, year_established):
        if isinstance(year_established, int):
            self.yearEstablished = year_established;
        else:
            raise ValueError("Year established must be an integer.");

    # Method to update and return the year established
    def WebsiteStartDate(self):
        self.yearEstablished += 1;
        return f"Website was established in {self.yearEstablished}";

    # String representation of the Website
    def __str__(self):
        return f"{self.title} is based in {self.location}";



