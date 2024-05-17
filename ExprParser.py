# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        42,8,1,10,1,12,1,45,9,1,1,2,1,2,1,2,1,2,3,2,51,8,2,1,3,1,3,3,3,55,
        8,3,1,4,1,4,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,3,4,66,8,4,1,4,1,
        4,1,5,1,5,1,5,1,5,3,5,74,8,5,1,6,1,6,1,6,1,6,3,6,80,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,91,8,7,1,8,1,8,1,8,3,8,96,8,8,1,
        9,1,9,1,9,5,9,101,8,9,10,9,12,9,104,9,9,1,10,1,10,1,11,1,11,1,12,
        1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,112,0,30,
        1,0,0,0,2,35,1,0,0,0,4,46,1,0,0,0,6,54,1,0,0,0,8,56,1,0,0,0,10,73,
        1,0,0,0,12,75,1,0,0,0,14,90,1,0,0,0,16,95,1,0,0,0,18,97,1,0,0,0,
        20,105,1,0,0,0,22,107,1,0,0,0,24,109,1,0,0,0,26,29,3,4,2,0,27,29,
        3,2,1,0,28,26,1,0,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,
        0,0,35,36,3,12,6,0,36,37,3,20,10,0,37,43,3,14,7,0,38,39,3,20,10,
        0,39,40,3,14,7,0,40,42,1,0,0,0,41,38,1,0,0,0,42,45,1,0,0,0,43,41,
        1,0,0,0,43,44,1,0,0,0,44,3,1,0,0,0,45,43,1,0,0,0,46,47,5,9,0,0,47,
        50,5,1,0,0,48,51,3,6,3,0,49,51,5,11,0,0,50,48,1,0,0,0,50,49,1,0,
        0,0,51,5,1,0,0,0,52,55,3,8,4,0,53,55,5,11,0,0,54,52,1,0,0,0,54,53,
        1,0,0,0,55,7,1,0,0,0,56,65,5,2,0,0,57,62,3,10,5,0,58,59,5,3,0,0,
        59,61,3,10,5,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,
        0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,65,57,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,68,5,4,0,0,68,9,1,0,0,0,69,74,5,10,0,0,70,74,5,12,
        0,0,71,72,5,5,0,0,72,74,5,12,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,
        71,1,0,0,0,74,11,1,0,0,0,75,79,5,9,0,0,76,77,5,2,0,0,77,78,5,12,
        0,0,78,80,5,4,0,0,79,76,1,0,0,0,79,80,1,0,0,0,80,13,1,0,0,0,81,82,
        5,9,0,0,82,83,3,22,11,0,83,84,3,18,9,0,84,85,3,24,12,0,85,91,1,0,
        0,0,86,87,5,9,0,0,87,88,3,22,11,0,88,89,3,24,12,0,89,91,1,0,0,0,
        90,81,1,0,0,0,90,86,1,0,0,0,91,15,1,0,0,0,92,96,3,10,5,0,93,96,5,
        11,0,0,94,96,3,8,4,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,
        17,1,0,0,0,97,102,3,16,8,0,98,99,5,3,0,0,99,101,3,16,8,0,100,98,
        1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,19,1,
        0,0,0,104,102,1,0,0,0,105,106,5,6,0,0,106,21,1,0,0,0,107,108,5,7,
        0,0,108,23,1,0,0,0,109,110,5,8,0,0,110,25,1,0,0,0,12,28,30,43,50,
        54,62,65,73,79,90,95,102
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "','", "']'", "'-'", "'|>'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR_NAME", "FLOAT", "STRING", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_expression = 1
    RULE_variable_assignment = 2
    RULE_variable_value = 3
    RULE_array_value = 4
    RULE_number = 5
    RULE_variable_access = 6
    RULE_function_call = 7
    RULE_arg = 8
    RULE_args = 9
    RULE_single_pipe_symbol = 10
    RULE_left_par = 11
    RULE_right_par = 12

    ruleNames =  [ "prog", "expression", "variable_assignment", "variable_value", 
                   "array_value", "number", "variable_access", "function_call", 
                   "arg", "args", "single_pipe_symbol", "left_par", "right_par" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    VAR_NAME=9
    FLOAT=10
    STRING=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def variable_assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Variable_assignmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.Variable_assignmentContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.variable_assignment()
                    pass

                elif la_ == 2:
                    self.state = 27
                    self.expression()
                    pass


                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_access(self):
            return self.getTypedRuleContext(ExprParser.Variable_accessContext,0)


        def single_pipe_symbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Single_pipe_symbolContext)
            else:
                return self.getTypedRuleContext(ExprParser.Single_pipe_symbolContext,i)


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Function_callContext)
            else:
                return self.getTypedRuleContext(ExprParser.Function_callContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.variable_access()
            self.state = 36
            self.single_pipe_symbol()
            self.state = 37
            self.function_call()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 38
                self.single_pipe_symbol()
                self.state = 39
                self.function_call()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(ExprParser.VAR_NAME, 0)

        def variable_value(self):
            return self.getTypedRuleContext(ExprParser.Variable_valueContext,0)


        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variable_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_assignment" ):
                listener.enterVariable_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_assignment" ):
                listener.exitVariable_assignment(self)




    def variable_assignment(self):

        localctx = ExprParser.Variable_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExprParser.VAR_NAME)
            self.state = 47
            self.match(ExprParser.T__0)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
                self.variable_value()
                pass

            elif la_ == 2:
                self.state = 49
                self.match(ExprParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_value(self):
            return self.getTypedRuleContext(ExprParser.Array_valueContext,0)


        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variable_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_value" ):
                listener.enterVariable_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_value" ):
                listener.exitVariable_value(self)




    def variable_value(self):

        localctx = ExprParser.Variable_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_value)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.array_value()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(ExprParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.NumberContext)
            else:
                return self.getTypedRuleContext(ExprParser.NumberContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_array_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_value" ):
                listener.enterArray_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_value" ):
                listener.exitArray_value(self)




    def array_value(self):

        localctx = ExprParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ExprParser.T__1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5152) != 0):
                self.state = 57
                self.number()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 58
                    self.match(ExprParser.T__2)
                    self.state = 59
                    self.number()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 67
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = ExprParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(ExprParser.FLOAT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(ExprParser.INT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(ExprParser.T__4)
                self.state = 72
                self.match(ExprParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.index = None # Token

        def VAR_NAME(self):
            return self.getToken(ExprParser.VAR_NAME, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variable_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_access" ):
                listener.enterVariable_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_access" ):
                listener.exitVariable_access(self)




    def variable_access(self):

        localctx = ExprParser.Variable_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ExprParser.VAR_NAME)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 76
                self.match(ExprParser.T__1)
                self.state = 77
                localctx.index = self.match(ExprParser.INT)
                self.state = 78
                self.match(ExprParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(ExprParser.VAR_NAME, 0)

        def left_par(self):
            return self.getTypedRuleContext(ExprParser.Left_parContext,0)


        def args(self):
            return self.getTypedRuleContext(ExprParser.ArgsContext,0)


        def right_par(self):
            return self.getTypedRuleContext(ExprParser.Right_parContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = ExprParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_call)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(ExprParser.VAR_NAME)
                self.state = 82
                self.left_par()
                self.state = 83
                self.args()
                self.state = 84
                self.right_par()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(ExprParser.VAR_NAME)
                self.state = 87
                self.left_par()
                self.state = 88
                self.right_par()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ExprParser.NumberContext,0)


        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def array_value(self):
            return self.getTypedRuleContext(ExprParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)




    def arg(self):

        localctx = ExprParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arg)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 10, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.number()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(ExprParser.STRING)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.array_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArgContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArgContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = ExprParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.arg()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 98
                self.match(ExprParser.T__2)
                self.state = 99
                self.arg()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_pipe_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_single_pipe_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_pipe_symbol" ):
                listener.enterSingle_pipe_symbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_pipe_symbol" ):
                listener.exitSingle_pipe_symbol(self)




    def single_pipe_symbol(self):

        localctx = ExprParser.Single_pipe_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_single_pipe_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ExprParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_left_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_par" ):
                listener.enterLeft_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_par" ):
                listener.exitLeft_par(self)




    def left_par(self):

        localctx = ExprParser.Left_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_left_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ExprParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_right_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_par" ):
                listener.enterRight_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_par" ):
                listener.exitRight_par(self)




    def right_par(self):

        localctx = ExprParser.Right_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_right_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





