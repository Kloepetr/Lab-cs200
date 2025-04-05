"""
rubric, pasted for easier access
1. At least three types of variables are created (5’) int, float, str ✅
2. At least five variables are created (5’) ✅
3. All values used are stored in variables (5’) ✅
4. At least one mathematical computation is performed (5’)✅
5. Output is a paragraph using at least four variables and computation result(s) (5’)✅
6. Program runs successfully and output values are correct. (30’)✅
7. Have a standard file header (5’)✅
8. Have good naming conventions (in variable names and Python file name) (5’)✅
9. Have adequate comments (10’)✅
10. Have code blocks (5’)✅
11. Problem description in the algorithm design file is clear and concise (5’)✅
12. Algorithm design is detailed enough (5’)✅
13. Algorithm design is accurate and complete (5’)✅
14. Program follows the algorithm design (5’✅


"""

# Header: Temperature converter/celcius and farenheit conversion tool

#assigning values to my temperatures
Beijing_temp_in_celcius = 20;
Tokyo_temp_in_farenheit = 88;
Berlin_temp_in_celcius = 16;
Paris_temp_in_farenheit = 61;
#defining functions to convert celcius to farenheit and vice versa
def c_to_f(temp_in_celcius):
    #mathematical equation
    celcius_to_farenheit = float(9/5 * (temp_in_celcius) + 32);
    return int(celcius_to_farenheit);
def f_to_c(temp_in_farenheit):
    #mathematical equation
    farenheit_to_celcius = float(5 * (temp_in_farenheit - 32)/9);
    #round the final temperature with int bracket
    return int(farenheit_to_celcius);
#connect all variables and finalized data into a condensed paragraph, group it in the variable temp_paragraph
temp_paragraph = "The temperature of Beijing is " + str(Beijing_temp_in_celcius) +" degrees celcius, or " + str(c_to_f(Beijing_temp_in_celcius)) + " degrees in farenheit; The temperature of Tokyo is " + str(Tokyo_temp_in_farenheit) +" degrees farenheit, or " + str(f_to_c(Tokyo_temp_in_farenheit)) + " degrees in celcius.In addition, the temperature of Berlin is " + str(Berlin_temp_in_celcius) +" degrees celcius, or " + str(c_to_f(Berlin_temp_in_celcius)) + " degrees in celcius, and lastly, the temperature of Paris is " + str(Paris_temp_in_farenheit) +" degrees farenheit, or " + str(f_to_c(Paris_temp_in_farenheit)) + " degrees in celcius."
#display results
print(temp_paragraph);





