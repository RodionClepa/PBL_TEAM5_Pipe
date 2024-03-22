grammar Expr;
prog: pipeline_def var_def pipe_block EOF ;
pipeline_flag: 'pipe';
arg: (INT | CHAR | STRING | FLOAT | VAR_NAME);
args: arg (comma space* arg)*;
function_args: left_par args right_par;
function_name: VAR_NAME;
pipeline_def: pipeline_flag space function_name left_par right_par two_points
            | pipeline_flag space function_name function_args two_points;
single_pipe_symbol: '|>';
double_pipe_symbol: '||>';
tripple_pipe_symbol: '|||>';
pipe: tab single_pipe_symbol space function_name left_par right_par
    | tab double_pipe_symbol space function_name left_par right_par
    | tab tripple_pipe_symbol space function_name left_par right_par
    | tab single_pipe_symbol space function_name function_args
    | tab double_pipe_symbol space function_name function_args
    | tab tripple_pipe_symbol space function_name function_args;
pipe_block: pipe (pipe)*;
tab: '    ';
space: ' ';
left_par: '(';
right_par: ')';
comma: ',';
two_points: ':';
var_name: VAR_NAME | CHAR;
var_def: tab var_name;




NEWLINE : [\r\n]+ -> skip ;
INT     : [0-9]+ ;
CHAR    : [a-zA-Z] ;
STRING  : ['][a-zA-Z]+['] ;
FLOAT   : [0-9]+[.][0-9]+ ;
VAR_NAME : [a-zA-Z][a-zA-Z0-9]* ;
COMMENT : '#' ~( '\r' | '\n' )* -> skip;

