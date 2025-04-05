"""Rubric
The required outputs are your first name ✅, your last name ✅,
your major ✅ , and a special character of your choice ✅ (punctuation marks and quotes do not count as special
characters). Use a .docx or .txt file to outline the algorithm design of your program.
1. Program runs successfully on PythonAnywhere. (30’) ✅
2. Program outputs the required items. (5’)✅
3. Program outputs are meaningful and well-organized. (10’)✅
4. Have at least three lines of output. (5’)✅
5. At least one special character is used and serves the purpose in the design of the output. (10’)✅
6. Have single line comments. (5’)✅
7. Have block comments. (5’)✅
8. Algorithm design is detailed enough. (10’)✅
9. Algorithm design is accurate and complete. (10’)✅
10. Program follows the algorithm design. (10’)✅
Submission
Submit your .py and algorithm design file on Canvas✅
"""
#assign values to my variables!
first_name = "kloe";
lastName = "Wang";
major = "computer science";
hobbies = "tennis, mini-golfing, ping-pong, listening to music, and thrifting";
school = "Indiana university, Indianapolis";
position= "student";
#print the output with introduction sentence
introduction="Hello, my name is " + first_name + " "+ lastName + "\nI am majoring in " + major + "," +" and I am currently a " + position + " at " + school + "."+ "\nMy hobbies are " + hobbies+".";
print(introduction);
# each line makes up the whole star print !
star_line1="         *        ";
star_line2="       *   *      ";
star_line3="      *     *     ";
star_line4=" * * *       * * *";
star_line5="   *           *  ";
star_line6="    *        *    ";
star_line7="   *     *     *  ";
star_line8="  *    *   *    * ";
star_line9=" *   *       *   *";
star_line10="* *           * *";
star = star_line1 +"\n" + star_line2+"\n" + star_line3+"\n" + star_line4+"\n" + star_line5+"\n" + star_line6+"\n" + star_line7+"\n" + star_line8+"\n" + star_line9+"\n" + star_line10+"\n";
#define star, then print the variable star.
print(star);
