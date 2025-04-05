'''
File Name: lab7.py
Purpose:

This file combines data from Contributions_to_oos_political_committees.csv and computes complete billing address
the csv file name is a bit long, but I want to keep the original csv file name from data.gov to avoid confusions.
First Create Date: October 29th, 2024
Last Update Date: October 29th, 2024
Author: Xiaoyuan Wang
Version: 1.1
'''
#import os module
import os;
#check if a file exists
print(os.path.exists("Contributions_to_oos_political_committees.csv"));
print(os.path.exists("/home/kloepetr/week8/Contributions_to_oos_political_committees.csv"));
#check if it is a directory
print(os.path.isdir("Contributions_to_oos_political_committees.csv"));
print(os.path.isdir("/home/kloepetr/week8"));
#check if it is a file
print(os.path.isfile("Contributions_to_oos_political_committees.csv"));
print(os.path.isfile("/home/kloepetr/week8"));

#import csv module
import csv
#create output directory
path = os.path.join(os.getcwd(),"output");
os.makedirs(path, exist_ok = True); #recursive call, create all directory needed for the path to exist
# Open the file in write mode
fout = open("output/Output.csv", 'w');
#open original csv file in read mode
opencsvfile = open("Contributions_to_oos_political_committees.csv", 'r');
# Write the header
header = "this is a list of contributions to out of state political committees."
fout.write(header + '\n')
#we will create a csv reader by creating a variable, read our input
csvreader = csv.reader(opencsvfile);
#set field to get next line in the csv file reader
#this gives us the first role and all the fields and create new column
field = next(csvreader);
#we can append the new data (column header)
field.append("committee address");
#we are creating an empty list to store the appended data
rows = [];
#we can use a for loop to access all the 2d array (rows) in the csv file
for row in csvreader:
    committee_address = "   " + row[5] + " " + row[6] + " " + row[7] + " " + row[8];
    row.append(committee_address);
    #we apply the appended list to every row
    rows.append(row);
# pass it in a variable, all csv writer need is a open csv file (line 14)
csvwriter = csv.writer(fout);
#we write all the field header
csvwriter.writerow(field);
#copy for every row
csvwriter.writerows(rows);
#add a footer
footer = "Author: Xiaoyuan Wang version: 1.1";
# Close both open files (security issues)
fout.write(footer + '\n');
fout.close();
opencsvfile.close();
