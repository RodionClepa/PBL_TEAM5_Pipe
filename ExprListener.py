# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_assignment.
    def enterVariable_assignment(self, ctx:ExprParser.Variable_assignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_assignment.
    def exitVariable_assignment(self, ctx:ExprParser.Variable_assignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_value.
    def enterVariable_value(self, ctx:ExprParser.Variable_valueContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_value.
    def exitVariable_value(self, ctx:ExprParser.Variable_valueContext):
        pass


    # Enter a parse tree produced by ExprParser#array_value.
    def enterArray_value(self, ctx:ExprParser.Array_valueContext):
        pass

    # Exit a parse tree produced by ExprParser#array_value.
    def exitArray_value(self, ctx:ExprParser.Array_valueContext):
        pass


    # Enter a parse tree produced by ExprParser#number.
    def enterNumber(self, ctx:ExprParser.NumberContext):
        pass

    # Exit a parse tree produced by ExprParser#number.
    def exitNumber(self, ctx:ExprParser.NumberContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_access.
    def enterVariable_access(self, ctx:ExprParser.Variable_accessContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_access.
    def exitVariable_access(self, ctx:ExprParser.Variable_accessContext):
        pass


    # Enter a parse tree produced by ExprParser#function_call.
    def enterFunction_call(self, ctx:ExprParser.Function_callContext):
        pass

    # Exit a parse tree produced by ExprParser#function_call.
    def exitFunction_call(self, ctx:ExprParser.Function_callContext):
        pass


    # Enter a parse tree produced by ExprParser#arg.
    def enterArg(self, ctx:ExprParser.ArgContext):
        pass

    # Exit a parse tree produced by ExprParser#arg.
    def exitArg(self, ctx:ExprParser.ArgContext):
        pass


    # Enter a parse tree produced by ExprParser#args.
    def enterArgs(self, ctx:ExprParser.ArgsContext):
        pass

    # Exit a parse tree produced by ExprParser#args.
    def exitArgs(self, ctx:ExprParser.ArgsContext):
        pass


    # Enter a parse tree produced by ExprParser#single_pipe_symbol.
    def enterSingle_pipe_symbol(self, ctx:ExprParser.Single_pipe_symbolContext):
        pass

    # Exit a parse tree produced by ExprParser#single_pipe_symbol.
    def exitSingle_pipe_symbol(self, ctx:ExprParser.Single_pipe_symbolContext):
        pass


    # Enter a parse tree produced by ExprParser#left_par.
    def enterLeft_par(self, ctx:ExprParser.Left_parContext):
        pass

    # Exit a parse tree produced by ExprParser#left_par.
    def exitLeft_par(self, ctx:ExprParser.Left_parContext):
        pass


    # Enter a parse tree produced by ExprParser#right_par.
    def enterRight_par(self, ctx:ExprParser.Right_parContext):
        pass

    # Exit a parse tree produced by ExprParser#right_par.
    def exitRight_par(self, ctx:ExprParser.Right_parContext):
        pass



del ExprParser