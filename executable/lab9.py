"""
File name: lab9.py
Purpose: This file serves as a utility file that will run my classes
Author: Xiaoyuan Wang
Create date: November 17th 2024
Last update date:November 19th 2024
version: 1.1
"""
#import child and parent class
from author import Author
from guestAuthor import GuestAuthor


author = Author("Jane", "Doe", 1980)
print("Author information:")
print(author)

# Invoke parent method
print(f"Author's age in 2024: {author.get_age(2024)}")
# Change a parent property value
author.first_name = "Janet"
print(f"Updated Author's name: {author}")
# guest author info
guest_author = GuestAuthor("John", "Smith", 1990, "2022-01-15", 3)
print("\nguest author's information:")
print(guest_author)

guest_author.add_article()
print(f"After adding an article: {guest_author.articles_contributed} articles contributed.")
# Change a child property value
guest_author.articles_contributed = 10
print(f"articles contributed bu guest author: {guest_author.articles_contributed}")
# Demonstrate method overwrite
print(f"Guest Author Info: {guest_author}")
# Calculate employment duration
print(f"Employment Duration : {guest_author.get_employment_duration(2024)} years")


