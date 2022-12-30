# implementation-of-lexical-analyzer-and-AST-using-python-lib
Objectives: 
•	Develop a program to implement lexical analyzer.
•	Develop a program to implement abstract syntax tree (AST).
•	How to use Regex and AST libraries for our problems 
Implementation:

I used the "re" header file to implement tokenization, using the "re.split()" function to create tokens of given expression and used "ast" header file to implement abstract syntax tree, using the "ast.parse()" function to create abstract syntax tree of given expression and at the end print tokens and AST of   user’s expression.
Functions
	 def  a_s_t(expression):
	Use for creating AST of given expression from user
	expression = user’s input.
	def  tokenization(expression):
	Use for creating tokens of given expression from user
	expression = user’s input.

Functional Commands:

	re.split ('\s|(\W)', expression)
	Use for tokenization of expression
	\s is used for matches Unicode whitespace characters (which includes [ \t\n\r\f\v], and many other characters.
	\W is used to match any character which is not a word character.

	ast.dump(ast.parse(expression), indent=4)
	Use for creating AST of expression
	Indent the each parse by 4 to visualize tree easily



Specifications:

•	Interpreter 

	PyCharm community

•	Programming Language

	Python 3.11

•	Operating System:

	Windows 8,8.1,10,11 x64 bit

•	Hardware required:

	Processor: Core i3 or more with 4 cores 
	Dedicated video memory (at least 1 GB)
	Ram: 4 GB Ram
	Hard Disk: 100GB

Working of Code:

When the user run the program, it will prompt a user “enter the expression” after entering the expression and presses enter, after pressing the enter key, a menu will appear to the user, in which there will be 2 options. 
1.	Enter 1 for tokenization of expression.
2.	Enter 2 for Abstract Syntax tree of expression.
Now the user can select any one of the options as per his wish. Option 1 will give him tokenization of expression and Option 2 will give him abstract syntax tree of his entered expression.
