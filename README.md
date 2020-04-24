JAVA PARSER
Group – 3
Sachin Pandey | 1701CS61
Vaibhav Pandey | 1701CS59
Umang Jain | 1701CS56

Status:

What we have implemented-
Our code can extract data from

1> 	All type of import statements.
2>	All types of class declaration and nested classes their attributes.
3> 	All type of expressions and initialization excepty array initialization .
4>	 All types of loops and their nesting and their initialization can be of 	any 	type like assignment or declaration and also it can be more than one, condition 	statement can be of any type and update can also be zero, one or more than 	one.
5>	All types of if else statements and their nestings with themselves as well as 	with the loops and also conditional statement can be of any type.
6>	All type of methods and their body.
7>	All types of Type Casting.

What our code cannot do:-

1>	Cannot Extract data from return statement.(Mainly If Ternary 	operator is used 	in return statement)
2>	Also cannot extract data variable assignment or declaration of any user defined 	class object.

Files:

java9.g4  :  java9 grammar
mytest.py : Main file
test.java : java code to parse
Readme.txt : Meta information file

Execution Instruction : Run          python3 mytest.py test.java

Github Link : https://github.com/umang1999/PPL_Lab5
