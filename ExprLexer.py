# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,136,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        4,8,59,8,8,11,8,12,8,60,1,8,1,8,4,8,65,8,8,11,8,12,8,66,3,8,69,8,
        8,1,9,4,9,72,8,9,11,9,12,9,73,1,9,1,9,4,9,78,8,9,11,9,12,9,79,1,
        9,1,9,4,9,84,8,9,11,9,12,9,85,1,9,1,9,4,9,90,8,9,11,9,12,9,91,3,
        9,94,8,9,1,10,1,10,1,10,1,10,1,11,1,11,5,11,102,8,11,10,11,12,11,
        105,9,11,1,11,1,11,1,12,4,12,110,8,12,11,12,12,12,111,1,12,1,12,
        1,13,1,13,5,13,118,8,13,10,13,12,13,121,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,132,8,14,1,15,1,15,1,15,0,0,16,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,1,0,10,1,0,48,57,1,0,45,45,1,0,46,46,1,0,34,34,3,0,48,
        57,65,90,97,122,3,0,9,10,13,13,32,32,2,0,65,90,97,122,4,0,48,57,
        65,90,95,95,97,122,1,0,124,124,1,0,62,62,147,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,
        0,3,38,1,0,0,0,5,45,1,0,0,0,7,47,1,0,0,0,9,49,1,0,0,0,11,51,1,0,
        0,0,13,53,1,0,0,0,15,55,1,0,0,0,17,68,1,0,0,0,19,93,1,0,0,0,21,95,
        1,0,0,0,23,99,1,0,0,0,25,109,1,0,0,0,27,115,1,0,0,0,29,131,1,0,0,
        0,31,133,1,0,0,0,33,34,5,102,0,0,34,35,5,114,0,0,35,36,5,111,0,0,
        36,37,5,109,0,0,37,2,1,0,0,0,38,39,5,105,0,0,39,40,5,109,0,0,40,
        41,5,112,0,0,41,42,5,111,0,0,42,43,5,114,0,0,43,44,5,116,0,0,44,
        4,1,0,0,0,45,46,5,40,0,0,46,6,1,0,0,0,47,48,5,41,0,0,48,8,1,0,0,
        0,49,50,5,61,0,0,50,10,1,0,0,0,51,52,5,91,0,0,52,12,1,0,0,0,53,54,
        5,93,0,0,54,14,1,0,0,0,55,56,5,44,0,0,56,16,1,0,0,0,57,59,7,0,0,
        0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,69,
        1,0,0,0,62,64,7,1,0,0,63,65,7,0,0,0,64,63,1,0,0,0,65,66,1,0,0,0,
        66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,58,1,0,0,0,68,62,1,
        0,0,0,69,18,1,0,0,0,70,72,7,0,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,
        71,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,7,2,0,0,76,78,7,0,0,
        0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,94,
        1,0,0,0,81,83,7,1,0,0,82,84,7,0,0,0,83,82,1,0,0,0,84,85,1,0,0,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,89,7,2,0,0,88,90,7,
        0,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,
        94,1,0,0,0,93,71,1,0,0,0,93,81,1,0,0,0,94,20,1,0,0,0,95,96,7,3,0,
        0,96,97,7,4,0,0,97,98,7,3,0,0,98,22,1,0,0,0,99,103,7,3,0,0,100,102,
        8,3,0,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,
        1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,7,3,0,0,107,24,1,
        0,0,0,108,110,7,5,0,0,109,108,1,0,0,0,110,111,1,0,0,0,111,109,1,
        0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,6,12,0,0,114,26,1,
        0,0,0,115,119,7,6,0,0,116,118,7,7,0,0,117,116,1,0,0,0,118,121,1,
        0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,28,1,0,0,0,121,119,1,0,
        0,0,122,123,5,116,0,0,123,124,5,114,0,0,124,125,5,117,0,0,125,132,
        5,101,0,0,126,127,5,102,0,0,127,128,5,97,0,0,128,129,5,108,0,0,129,
        130,5,115,0,0,130,132,5,101,0,0,131,122,1,0,0,0,131,126,1,0,0,0,
        132,30,1,0,0,0,133,134,7,8,0,0,134,135,7,9,0,0,135,32,1,0,0,0,13,
        0,60,66,68,73,79,85,91,93,103,111,119,131,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INT = 9
    FLOAT = 10
    CHAR = 11
    STRING = 12
    WS = 13
    NAME = 14
    BOOL = 15
    SPIPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'from'", "'import'", "'('", "')'", "'='", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "CHAR", "STRING", "WS", "NAME", "BOOL", "SPIPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INT", "FLOAT", "CHAR", "STRING", "WS", "NAME", 
                  "BOOL", "SPIPE" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


