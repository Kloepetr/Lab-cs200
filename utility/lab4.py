"""
#GAS-PRICE-CALCULATOR (header)
File Name: lab4.py
Purpose:
This file calls out the functions imported from the file gasPriceConvertion;
First Create Date: september 20th , 2024
Last Update Date: September 22nd , 2024
Author: Xiaoyuan Wang
Version: 1.1
#GAS-PRICE-CONVERTION (header)
this is an executable file that aims to convert gas type to its price
project objectives
1. Ask for at least two keyboard inputs(10’)  yes
2. If/else structure is used. (10’) yes
3. Each choice is defined as a function and the functions are called in the executable file. (10’) yes
4. Have a utility file and group all the function definitions that should be grouped in this file. (5’) yes
5. Take invalid inputs into considerations. E.g. if an input should be numeric, only process the input
if it is indeed numeric. (5’)
6. Program runs successfully and generates meaningful outputs. (30’)
7. Follow professional coding standards (file headers, comments, code blocks, naming conventions,
etc). (10’)
8. Use pseudocodes to describe your algorithm design in a .docx file. Your code must follow the
algorithm design. Your pseudocodes must be more similar to the Python language rather than
the English language. See sample pseudocode file named “keyboardInputPseudocode.txt”
a) Pseudocodes are used (5’)
b) Algorithm design is detailed enough. Must also have algorithm design for each
function. (5’)
c) Algorithm design is accurate and complete. (5’)
d) Program follows the algorithm design. (5’)
"""

#import my executable file
from gasPriceConvertion import gasPriceConvertion;

#first user input, second one is in the executable file.
gas_type = input("What kind of gas are you pumping ?\nHint: enter letter 'r' for regular gas, letters 'mg' for mid-grade gas , or letter 'p' for premium gas \n");
#final price in complete sentence'
print("the price of your gas is " + gasPriceConvertion(gas_type));
