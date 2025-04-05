"""
File name: lab8.py
Purpose: This file serves as a utility file that will run my classes
Author: Xiaoyuan Wang
Create date: November 11th 2024
Last update date:November 12th 2024
version: 1.1
"""
#import my modules
from author import Author
from category import Category
from website import Website

# Testing the classes
if __name__ == "__main__":
    # Creating instances of Author and Website
    author1 = Author("Thomas", "Johnson", 1995)
    website1 = Website("The New Yorkers", "New York", 1925)
    category1 = Category("How to Deal with Anxiety", "Mental Health", "Self Care", author1)


#originial website information and start date
print("Website information:", website1)
print(website1.WebsiteStartDate())
#updated website information using setter
website1.set_title("The Washington Post");
website1.set_location("Washington, D.C.");
website1.set_year_established(1890);
print("Updated Website Information: ", website1);
print(f'{author1} His article over "{category1.articleTitle}" explores his take on {category1.topic} and explores the genre of {category1.genre}.')
