import sys
# from inspect import signature
from antlr4 import *
from gen.CLexer import CLexer
# from CListener import CListener
from gen.java9Parser import java9Parser
from gen.java9Visitor import java9Visitor
import json

class Myjava9Visitor(java9Visitor):
    pass


class Myjava9Visitor2(java9Visitor):
    pass





def main(argv):

    inputFile = FileStream(argv[1])
    lexer = java9Lexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = java9Parser(stream)
    tree = parser.compilationUnit()

    v = Myjava9Visitor2()
    v.visit(tree)


    x = {"name": "", "class": [], "class_type": ""}

    x["class"].extend(x)
    print(x)

if __name__ == '__main__':
    main(sys.argv)