"""
File name: studentClass.py
Purpose: This file defines the student class
Author: Xiaoyuan Wang
Create date: November 10th 2024
Last update date:November 12th 2024
version: 1.1
"""

from diplomaClass import diploma;

class Employee:
    #define properties
    firstName = "";
    lastName = "";
    graduationYear = "";
    diploma = diploma();


    #define methods
    #always have a "constructor" method that will set the property values; "self" refers to the object instance, it can be any text value, but must be the first parameter
    def __init__(self, fn, ln, gy, d):
        self.firstName = fn;
        self.lastName = ln;
        self.graduationYear = gy;
        self.diploma = d;

    #always define a str function so that when the object is used as a string, the output will describe the object
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "; Graduation year: " + str(self.graduationYear) + ";  Diploma: "+ str(self.diploma);

    #It is a good idea to have a number of setters to set or change property values
    def setFirstName(s, fn):
        s.firstName = fn;

    def setLastName(s, ln):
        s.lastName = ln;

    def setAge(s, gy):
        s.graduationYear = gy;

    def setDiploma(s, d):
        s.diploma = d;


    #It is a good idea to have a number of getters to retrieve property values
    def getFirstName(s):
        return s.firstName;

    def getLastName(s):
        return s.lastName;

    def getGraduationYear(s):
        return s.graduationYear;

    def getDiploma(s):
        return s.Diploma;


    #define other methods that apply to the object
    def getName(s):
        return s.firstName + " " + s.lastName;
