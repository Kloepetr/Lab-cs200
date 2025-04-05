#MATHEMATICAL-CALCULATOR (header)
"""
project objective: create a calculator that can execute addition, multiplication, subtraction and division
requirements:
Design a program with a purpose and meet the following requirements:
1. Have at least 3 user defined functions (5’)
2. At least one function is called within another function (5’)
3. At least one function takes two parameters (5’)
4. At least one function returns a value (5’)
5. At least one global variable is used and accessed inside a function (5’)
6. Program runs successfully (30’)
7. Program generates correct and meaningful output (5’)
8. Have a standard file header (5’)
9. Have good naming conventions (variable names, function names, file name) (5’)
10. Have adequate comments (5’)
11. Have meaningful code blocks (10’)
"""


#assign values to my global variables in order to be accessed later.
A = 1;
B = 2;
C = 3;
D = 4;

#user defined function "adding_numbers"
def adding_numbers(x, y):
    #assig
    add_num = x + y ;
    #the sum of the argument x and y is being returned
    return add_num;
#user defined function "subtracting_numbers"
def subtracting_numbers(x, y): #function defined two parameters
    minus_num = x - y ;
    #the result of the argument x and y being subtracted is being returned
    return minus_num;
#user defined function "multiplying_numbers"
def multiplying_numbers(x,y):
    #the result of the argument x and y multiplying is being returned
    multiply_num = x * y;
    return multiply_num;
#user defined function "dividing_numbers"
def dividing_numbers(x, y):
    #the result of the arguments x and y dividing each other is being returned
    divide_num = x / y;
    #dividing between the numbers could result in a number involving decimals, therefore, add a string bracket
    return str(divide_num);

def output():
    #calling my functions within the function output
    print("A plus B equals " + str(adding_numbers(A,B))); #since function was defined with two parameters, it requires two arguments passed into the function)
    print("B plus C equals " + str(subtracting_numbers(B,C)));#since function was defined with two parameters, it requires two arguments passed into the function)
    print("D plus C equals " + str(multiplying_numbers(D,C)));#since function was defined with two parameters, it requires two arguments passed into the function)
    print("B plus C equals " + str(dividing_numbers(B,C)));#since function was defined with two parameters, it requires two arguments passed into the function)


output()

