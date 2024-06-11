# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

from FunctionHandler import FunctionHandler

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    class variable:
        def __init__(self, name, value=None, type=None):
            self.name = name
            self.value = value
            self.type = type

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.variables = []
        self.current_variable = None
        self.function_handler = FunctionHandler()

    def add_variable(self, variable):
        for var in self.variables:
            if var.name == variable.name:
                var.value = variable.value
                var.type = variable.type
                return

        self.variables.append(variable)

    def get_var(self, name):
        for variable in self.variables:
            if variable.name == name:
                return variable
        return None

    def get_var_value(self, var):
        if var.INT():
            return int(var.INT().getText())
        elif var.FLOAT():
            return float(var.FLOAT().getText())
        elif var.CHAR():
            return var.CHAR().getText().replace("'", '')
        elif var.STRING():
            return var.STRING().getText().replace('"', '')
        elif var.BOOL():
            return var.BOOL().getText() == 'true'
        elif var.NAME():
            var = self.get_var(var.NAME().getText())
            if var:
                return var.value
            else:
                raise Exception("Variable not found")
        else:
            raise Exception("Invalid type")

    def get_type(self, var):
        if var.INT():
            return 'int'
        elif var.FLOAT():
            return 'float'
        elif var.CHAR():
            return 'char'
        elif var.STRING():
            return 'str'
        elif var.BOOL():
            return 'bool'
        else:
            pass

    def parse_arrays(self, ctx):
        arr = []
        for child in ctx.children:
            if child in ctx.value():
                # print("value -> ", child.getText())
                arr.append(self.get_var_value(child))
            elif child in ctx.array():
                # print("array -> ", child.getText())
                arr.append(self.parse_arrays(child))
        return arr

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        for var in self.variables: print(f'{var.name} => {var.value} ({var.type})')
        pass


    # Enter a parse tree produced by ExprParser#imports.
    def enterImports(self, ctx:ExprParser.ImportsContext):
        pass


    # Exit a parse tree produced by ExprParser#imports.
    def exitImports(self, ctx:ExprParser.ImportsContext):
        pass


    # Enter a parse tree produced by ExprParser#import_statement.
    def enterImport_statement(self, ctx:ExprParser.Import_statementContext):
        import importlib


        file_name = ctx.NAME()[0].getText()
        function_name = ctx.NAME()[1].getText()

        module = importlib.import_module(file_name)
        function = getattr(module, function_name)



        self.function_handler.add_function(function_name, function)





    # Exit a parse tree produced by ExprParser#import_statement.
    def exitImport_statement(self, ctx:ExprParser.Import_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#single_pipe_statement.
    def enterSingle_pipe_statement(self, ctx:ExprParser.Single_pipe_statementContext):
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        print("-----------------------------")
        print(f'{var_name} = {var.value}')

        if not var:
            raise Exception("Variable not found")

        for function in ctx.function_call():
            if function.NAME().getText() == 'print':
                print(var.value)
            else:
                args = []
                if function.args():
                    for arg in function.args().value():
                        args.append(self.get_var_value(arg))
                print("->", var)
                result = self.function_handler.execute(var.value, function.NAME().getText(), args)
                print(f"----> ({function.NAME().getText()})", result)
                result_type = type(result).__name__
                var.value = result
                var.type = result_type


        print(f'{var_name} = {var.value}')
        print("-----------------------------")

    # Exit a parse tree produced by ExprParser#single_pipe_statement.
    def exitSingle_pipe_statement(self, ctx:ExprParser.Single_pipe_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#function_call.
    def enterFunction_call(self, ctx:ExprParser.Function_callContext):
        pass

    # Exit a parse tree produced by ExprParser#function_call.
    def exitFunction_call(self, ctx:ExprParser.Function_callContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        arr = []
        var_name = ctx.NAME().getText()
        var = self.get_var(var_name)

        if var:
            self.current_variable = var
        else:
            self.current_variable = self.variable(var_name)

        if ctx.value():
            if ctx.value().INT():
                self.current_variable.value = int(ctx.value().INT().getText())
                self.current_variable.type = 'int'
            elif ctx.value().FLOAT():
                self.current_variable.value = float(ctx.value().FLOAT().getText())
                self.current_variable.type = 'float'
            elif ctx.value().CHAR():
                self.current_variable.value = ctx.value().CHAR().getText().replace("'", '')
                self.current_variable.type = 'char'
            elif ctx.value().STRING():
                self.current_variable.value = ctx.value().STRING().getText().replace('"', '')
                self.current_variable.type = 'str'
            elif ctx.value().BOOL():
                self.current_variable.value = ctx.value().BOOL().getText() == 'true'
                self.current_variable.type = 'bool'
            else:
                raise Exception("Invalid type")
        elif ctx.array():
            self.current_variable.value = self.parse_arrays(ctx.array())
            self.current_variable.type = 'list'
        else:
            raise Exception("Invalid type")

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        self.add_variable(self.current_variable)
        self.current_variable = None


    # Enter a parse tree produced by ExprParser#array.
    def enterArray(self, ctx:ExprParser.ArrayContext):
        pass

    # Exit a parse tree produced by ExprParser#array.
    def exitArray(self, ctx:ExprParser.ArrayContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass


    # Enter a parse tree produced by ExprParser#args.
    def enterArgs(self, ctx:ExprParser.ArgsContext):
        pass

    # Exit a parse tree produced by ExprParser#args.
    def exitArgs(self, ctx:ExprParser.ArgsContext):
        pass



del ExprParser