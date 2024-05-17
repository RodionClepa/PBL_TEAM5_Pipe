from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

def main():
    input_stream = InputStream("your_input_here")
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.prog()

    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
