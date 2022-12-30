# Muhammad Usman  Reg# 200901104  Assign_02 CC   BS-CS-01-A
import re  # importing regex lib
import ast  # importing AST lib


def a_s_t(expression):
    print("\nAST Module Executed")
    print("\nThe Expression: ", expression)
    abstract_syntax_tree = ast.dump(ast.parse(expression), indent=4)  # building AST for expressions
    print(abstract_syntax_tree)  # printing AST
    print("-------------------------------------------")


def tokenization(expression):
    print("\nTokenization Module Executed")
    print("\nThe Expression: ", expression)
    tokens = re.split('\s|(\W)', expression)  # building regex for expression
    print("\nTokens: ", list(filter(None, tokens)))  # filter the spacing and printing tokens
    print("-------------------------------------------")


if __name__ == '__main__':  # main body
    exp = input("\nEnter your expression: ")
    print("Enter 1 for Tokenization of ", exp)
    print("Enter 2 for Abstract Syntax Tree of ", exp)
    option = int(input("Enter your desire option"))
    if option == 1:
        tokenization(exp)  # calling func for tokenization
    elif option == 2:
        a_s_t(exp)  # calling func for AST
    else:
        exit()
