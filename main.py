from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

def parse_input(input_text):
    # Create an input stream from the input text
    input_stream = InputStream(input_text)
    
    # Create a lexer
    lexer = ExprLexer(input_stream)
    
    # Create a token stream
    token_stream = CommonTokenStream(lexer)
    
    # Create a parser
    parser = ExprParser(token_stream)
    
    # Invoke the entry rule
    tree = parser.prog()  # Replace 'startRule' with the name of your entry rule
    
    # If no parsing error occurred, the input is valid
    return not parser.getNumberOfSyntaxErrors()

# Read input from a text file
file_path = 'Test.txt'
with open(file_path, 'r') as file:
    input_text = file.read()

# Test if the input text is valid according to your grammar
if parse_input(input_text):
    print("Input is valid!")
else:
    print("Input is not valid!")
