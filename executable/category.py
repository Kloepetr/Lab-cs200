"""
File name: category.py
Purpose: This file defines category class
Author: Xiaoyuan Wang
Create date: November 11th 2024
Last update date: November 12th, 2024
version: 1.1
"""
class Category:
    def __init__(self, at, t, g, author):
        self.articleTitle = at;
        self.topic = t;
        self.genre = g;
        # Instance of Author class;
        self.author = author;

    # Method to get article genre
    def get_article_genre(self):
        return (f'The article genre is {self.genre}');
    def get_article_topic(self):
        return(f'The article topic is {self.topic}');



