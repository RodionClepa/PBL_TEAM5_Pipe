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


    # Enter a parse tree produced by ExprParser#pipeline_flag.
    def enterPipeline_flag(self, ctx:ExprParser.Pipeline_flagContext):
        pass

    # Exit a parse tree produced by ExprParser#pipeline_flag.
    def exitPipeline_flag(self, ctx:ExprParser.Pipeline_flagContext):
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


    # Enter a parse tree produced by ExprParser#function_args.
    def enterFunction_args(self, ctx:ExprParser.Function_argsContext):
        pass

    # Exit a parse tree produced by ExprParser#function_args.
    def exitFunction_args(self, ctx:ExprParser.Function_argsContext):
        pass


    # Enter a parse tree produced by ExprParser#function_name.
    def enterFunction_name(self, ctx:ExprParser.Function_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#function_name.
    def exitFunction_name(self, ctx:ExprParser.Function_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#pipeline_def.
    def enterPipeline_def(self, ctx:ExprParser.Pipeline_defContext):
        pass

    # Exit a parse tree produced by ExprParser#pipeline_def.
    def exitPipeline_def(self, ctx:ExprParser.Pipeline_defContext):
        pass


    # Enter a parse tree produced by ExprParser#single_pipe_symbol.
    def enterSingle_pipe_symbol(self, ctx:ExprParser.Single_pipe_symbolContext):
        pass

    # Exit a parse tree produced by ExprParser#single_pipe_symbol.
    def exitSingle_pipe_symbol(self, ctx:ExprParser.Single_pipe_symbolContext):
        pass


    # Enter a parse tree produced by ExprParser#double_pipe_symbol.
    def enterDouble_pipe_symbol(self, ctx:ExprParser.Double_pipe_symbolContext):
        pass

    # Exit a parse tree produced by ExprParser#double_pipe_symbol.
    def exitDouble_pipe_symbol(self, ctx:ExprParser.Double_pipe_symbolContext):
        pass


    # Enter a parse tree produced by ExprParser#tripple_pipe_symbol.
    def enterTripple_pipe_symbol(self, ctx:ExprParser.Tripple_pipe_symbolContext):
        pass

    # Exit a parse tree produced by ExprParser#tripple_pipe_symbol.
    def exitTripple_pipe_symbol(self, ctx:ExprParser.Tripple_pipe_symbolContext):
        pass


    # Enter a parse tree produced by ExprParser#pipe.
    def enterPipe(self, ctx:ExprParser.PipeContext):
        pass

    # Exit a parse tree produced by ExprParser#pipe.
    def exitPipe(self, ctx:ExprParser.PipeContext):
        pass


    # Enter a parse tree produced by ExprParser#pipe_block.
    def enterPipe_block(self, ctx:ExprParser.Pipe_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#pipe_block.
    def exitPipe_block(self, ctx:ExprParser.Pipe_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#tab.
    def enterTab(self, ctx:ExprParser.TabContext):
        pass

    # Exit a parse tree produced by ExprParser#tab.
    def exitTab(self, ctx:ExprParser.TabContext):
        pass


    # Enter a parse tree produced by ExprParser#space.
    def enterSpace(self, ctx:ExprParser.SpaceContext):
        pass

    # Exit a parse tree produced by ExprParser#space.
    def exitSpace(self, ctx:ExprParser.SpaceContext):
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


    # Enter a parse tree produced by ExprParser#comma.
    def enterComma(self, ctx:ExprParser.CommaContext):
        pass

    # Exit a parse tree produced by ExprParser#comma.
    def exitComma(self, ctx:ExprParser.CommaContext):
        pass


    # Enter a parse tree produced by ExprParser#two_points.
    def enterTwo_points(self, ctx:ExprParser.Two_pointsContext):
        pass

    # Exit a parse tree produced by ExprParser#two_points.
    def exitTwo_points(self, ctx:ExprParser.Two_pointsContext):
        pass


    # Enter a parse tree produced by ExprParser#var_name.
    def enterVar_name(self, ctx:ExprParser.Var_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#var_name.
    def exitVar_name(self, ctx:ExprParser.Var_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#var_def.
    def enterVar_def(self, ctx:ExprParser.Var_defContext):
        pass

    # Exit a parse tree produced by ExprParser#var_def.
    def exitVar_def(self, ctx:ExprParser.Var_defContext):
        pass



del ExprParser