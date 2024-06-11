grammar Expr;

prog: imports (assignment single_pipe_statement*)+;

imports: import_statement*;

import_statement: 'from' NAME 'import' NAME;

single_pipe_statement: NAME (SPIPE function_call)+;

function_call: NAME '(' args ')' | NAME '(' ')';

assignment: NAME '=' (value | array);

array: '[' ']' | '[' (value | array) (',' (value | array))* ']';

value: INT | FLOAT | STRING | BOOL | CHAR | NAME;

args: (value | array) (',' (value | array))*;

INT: [0-9]+ | [-][0-9]+;
FLOAT: [0-9]+[.][0-9]+ | [-][0-9]+[.][0-9]+;
CHAR: ["][a-zA-Z0-9]["];
STRING: ["]~["]*["];
WS: [ \t\r\n]+ -> skip;
NAME: [a-zA-Z][a-zA-Z0-9_]*;
BOOL: 'true' | 'false';
SPIPE: [|][>];