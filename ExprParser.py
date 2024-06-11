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
        4,1,16,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,4,0,27,
        8,0,11,0,12,0,28,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,4,3,45,8,3,11,3,12,3,46,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,57,8,4,1,5,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,
        6,3,6,70,8,6,1,6,1,6,1,6,3,6,75,8,6,5,6,77,8,6,10,6,12,6,80,9,6,
        1,6,1,6,3,6,84,8,6,1,7,1,7,1,8,1,8,3,8,90,8,8,1,8,1,8,1,8,3,8,95,
        8,8,5,8,97,8,8,10,8,12,8,100,9,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,
        0,1,2,0,9,12,14,15,105,0,18,1,0,0,0,2,33,1,0,0,0,4,36,1,0,0,0,6,
        41,1,0,0,0,8,56,1,0,0,0,10,58,1,0,0,0,12,83,1,0,0,0,14,85,1,0,0,
        0,16,89,1,0,0,0,18,26,3,2,1,0,19,23,3,10,5,0,20,22,3,6,3,0,21,20,
        1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,26,19,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,
        0,0,0,29,1,1,0,0,0,30,32,3,4,2,0,31,30,1,0,0,0,32,35,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,0,0,36,37,5,1,0,
        0,37,38,5,14,0,0,38,39,5,2,0,0,39,40,5,14,0,0,40,5,1,0,0,0,41,44,
        5,14,0,0,42,43,5,16,0,0,43,45,3,8,4,0,44,42,1,0,0,0,45,46,1,0,0,
        0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,1,0,0,0,48,49,5,14,0,0,49,50,
        5,3,0,0,50,51,3,16,8,0,51,52,5,4,0,0,52,57,1,0,0,0,53,54,5,14,0,
        0,54,55,5,3,0,0,55,57,5,4,0,0,56,48,1,0,0,0,56,53,1,0,0,0,57,9,1,
        0,0,0,58,59,5,14,0,0,59,62,5,5,0,0,60,63,3,14,7,0,61,63,3,12,6,0,
        62,60,1,0,0,0,62,61,1,0,0,0,63,11,1,0,0,0,64,65,5,6,0,0,65,84,5,
        7,0,0,66,69,5,6,0,0,67,70,3,14,7,0,68,70,3,12,6,0,69,67,1,0,0,0,
        69,68,1,0,0,0,70,78,1,0,0,0,71,74,5,8,0,0,72,75,3,14,7,0,73,75,3,
        12,6,0,74,72,1,0,0,0,74,73,1,0,0,0,75,77,1,0,0,0,76,71,1,0,0,0,77,
        80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,
        0,81,82,5,7,0,0,82,84,1,0,0,0,83,64,1,0,0,0,83,66,1,0,0,0,84,13,
        1,0,0,0,85,86,7,0,0,0,86,15,1,0,0,0,87,90,3,14,7,0,88,90,3,12,6,
        0,89,87,1,0,0,0,89,88,1,0,0,0,90,98,1,0,0,0,91,94,5,8,0,0,92,95,
        3,14,7,0,93,95,3,12,6,0,94,92,1,0,0,0,94,93,1,0,0,0,95,97,1,0,0,
        0,96,91,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,17,
        1,0,0,0,100,98,1,0,0,0,13,23,28,33,46,56,62,69,74,78,83,89,94,98
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'from'", "'import'", "'('", "')'", "'='", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "CHAR", "STRING", "WS", 
                      "NAME", "BOOL", "SPIPE" ]

    RULE_prog = 0
    RULE_imports = 1
    RULE_import_statement = 2
    RULE_single_pipe_statement = 3
    RULE_function_call = 4
    RULE_assignment = 5
    RULE_array = 6
    RULE_value = 7
    RULE_args = 8

    ruleNames =  [ "prog", "imports", "import_statement", "single_pipe_statement", 
                   "function_call", "assignment", "array", "value", "args" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT=9
    FLOAT=10
    CHAR=11
    STRING=12
    WS=13
    NAME=14
    BOOL=15
    SPIPE=16

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

        def imports(self):
            return self.getTypedRuleContext(ExprParser.ImportsContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.AssignmentContext,i)


        def single_pipe_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Single_pipe_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Single_pipe_statementContext,i)


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
            self.state = 18
            self.imports()
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.assignment()
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 20
                        self.single_pipe_statement() 
                    self.state = 25
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Import_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Import_statementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImports" ):
                listener.enterImports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImports" ):
                listener.exitImports(self)




    def imports(self):

        localctx = ExprParser.ImportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_imports)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 30
                self.import_statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NAME)
            else:
                return self.getToken(ExprParser.NAME, i)

        def getRuleIndex(self):
            return ExprParser.RULE_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_statement" ):
                listener.enterImport_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_statement" ):
                listener.exitImport_statement(self)




    def import_statement(self):

        localctx = ExprParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_import_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ExprParser.T__0)
            self.state = 37
            self.match(ExprParser.NAME)
            self.state = 38
            self.match(ExprParser.T__1)
            self.state = 39
            self.match(ExprParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_pipe_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ExprParser.NAME, 0)

        def SPIPE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SPIPE)
            else:
                return self.getToken(ExprParser.SPIPE, i)

        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Function_callContext)
            else:
                return self.getTypedRuleContext(ExprParser.Function_callContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_single_pipe_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_pipe_statement" ):
                listener.enterSingle_pipe_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_pipe_statement" ):
                listener.exitSingle_pipe_statement(self)




    def single_pipe_statement(self):

        localctx = ExprParser.Single_pipe_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_single_pipe_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ExprParser.NAME)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.match(ExprParser.SPIPE)
                self.state = 43
                self.function_call()
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

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

        def NAME(self):
            return self.getToken(ExprParser.NAME, 0)

        def args(self):
            return self.getTypedRuleContext(ExprParser.ArgsContext,0)


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
        self.enterRule(localctx, 8, self.RULE_function_call)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ExprParser.NAME)
                self.state = 49
                self.match(ExprParser.T__2)
                self.state = 50
                self.args()
                self.state = 51
                self.match(ExprParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(ExprParser.NAME)
                self.state = 54
                self.match(ExprParser.T__2)
                self.state = 55
                self.match(ExprParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ExprParser.NAME, 0)

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def array(self):
            return self.getTypedRuleContext(ExprParser.ArrayContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ExprParser.NAME)
            self.state = 59
            self.match(ExprParser.T__4)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 14, 15]:
                self.state = 60
                self.value()
                pass
            elif token in [6]:
                self.state = 61
                self.array()
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueContext,i)


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArrayContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArrayContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = ExprParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(ExprParser.T__5)
                self.state = 65
                self.match(ExprParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(ExprParser.T__5)
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10, 11, 12, 14, 15]:
                    self.state = 67
                    self.value()
                    pass
                elif token in [6]:
                    self.state = 68
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 71
                    self.match(ExprParser.T__7)
                    self.state = 74
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9, 10, 11, 12, 14, 15]:
                        self.state = 72
                        self.value()
                        pass
                    elif token in [6]:
                        self.state = 73
                        self.array()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(ExprParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def NAME(self):
            return self.getToken(ExprParser.NAME, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueContext,i)


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArrayContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArrayContext,i)


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
        self.enterRule(localctx, 16, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 14, 15]:
                self.state = 87
                self.value()
                pass
            elif token in [6]:
                self.state = 88
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 91
                self.match(ExprParser.T__7)
                self.state = 94
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10, 11, 12, 14, 15]:
                    self.state = 92
                    self.value()
                    pass
                elif token in [6]:
                    self.state = 93
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





