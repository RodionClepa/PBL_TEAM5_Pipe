from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser 
from MyPipes import myPipe 

class MyListener(ParseTreeListener):
    def __init__(self):
        self.listPipe = {}

    def enterFunction_call(self, ctx):
        function_name = ctx.VAR_NAME().getText()

        varName = ctx.parentCtx.getText()
        varName = varName[0:varName.find("|")]

        args_ctx = ctx.args()
        args = []
        if args_ctx is not None:
            for arg_ctx in args_ctx.arg():
                arg_text = arg_ctx.getText()
                
                token_re = arg_ctx.getToken(ExprParser.STRING, 0)
                if (token_re is not None):
                    arg_text = arg_text.replace('"', "")
                    arg_text = arg_text.replace("'", "")
                else:
                    arg_text = int(arg_text)
                args.append(arg_text)
                    

        # print(args)
        
        self.listPipe[varName].addPipeFunctions(function_name, args)
        # print(self.listPipe[varName].pipeFunctions)

    
    def enterArray_value(self, ctx):
        self.x = []
        array_elements = ctx.children  # Access all child nodes of the array_value context
        
        varName = ctx.parentCtx.parentCtx.getText()
        varName = varName[0:varName.find("=")]
        skip_symbol = ['[', ']', ',']
        for child in array_elements:
            value = child.getText()
            if value not in skip_symbol:
                if "." in value:
                    self.x.append(float(value))
                else:
                    self.x.append(int(value))
        self.type = "array"
        self.listPipe[varName] = myPipe(varName, self.x, self.type)
        

    def enterVariable_assignment(self, ctx):
        value = ctx.getChild(2).getText()
        if value.startswith('"') and value.endswith('"'):
            self.x = value[1:-1]
            self.type = "string"
            varName = ctx.getChild(0).getText()
            self.listPipe[varName] = myPipe(varName, self.x, self.type)


from antlr4.error.ErrorListener import ConsoleErrorListener
class MyErrorListener(ConsoleErrorListener):
    def __init__(self):
        super().__init__()
        self.has_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        print("Syntax error at line {0}:{1} - {2}".format(line, column, msg))

def main():
    input_stream = FileStream('Test.txt')
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)

    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)
    if error_listener.has_errors:
        print("Parsing encountered errors.")
        return

    try:
        tree = parser.prog()
        listener = MyListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        for i in listener.listPipe:
            listener.listPipe[i].executePipes()
    except Exception as e:
        print("Exception occurred during parsing:", e)

if __name__ == '__main__':
    main()
