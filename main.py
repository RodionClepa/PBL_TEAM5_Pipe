from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser


def main():
    # Read input from a file
    input_stream = FileStream("Test.txt")

    # Create lexer
    lexer = ExprLexer(input_stream)

    # Create token stream
    token_stream = CommonTokenStream(lexer)

    # Create parser
    parser = ExprParser(token_stream)

    # Start parsing from the initial rule (prog in this case)
    tree = parser.prog()

    # Do something with the parse tree if needed
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()
