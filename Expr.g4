grammar Expr;

prog: (variable_assignment | expression)* EOF ;

expression: variable_access single_pipe_symbol function_call (single_pipe_symbol function_call)* ;

variable_assignment: VAR_NAME '=' (variable_value | STRING) ;

variable_value: array_value | STRING ;

array_value: '[' (number (',' number)*)? ']' ;

number: FLOAT | INT | '-' INT ;

variable_access: VAR_NAME ('[' index=INT ']')? ;

function_call: VAR_NAME left_par args right_par | VAR_NAME left_par right_par ;

arg: number | STRING | array_value ;
args: arg (',' arg)* ;

single_pipe_symbol: '|>';

VAR_NAME: [a-zA-Z][a-zA-Z0-9]* ;
FLOAT   : [0-9]+[.][0-9]+ ;
left_par: '(' ;
right_par: ')' ;
STRING: '"' ~["]* '"' ;
INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;