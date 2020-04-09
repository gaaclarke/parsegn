grammar GN;
gn_file:       top_level_stmt* EOF;
top_level_stmt: rule_stmt
  | if_stmt
  | import_stmt
  ;
rule_stmt:  IDENT '(' string? ')' '{' field* '}';
field:      field_if | field_entry;
field_if:   'if' '(' bool_expr ')' '{' field* '}' field_else?;
field_else:   'else' '{' field* '}';
field_entry:      IDENT ('=' | '+=') expr;
expr: bool_type 
    | array 
    | string 
    | IDENT
    | expr '+' expr
    | IDENT '[' INDEX ']' // array
    | IDENT '(' (expr ',')* expr? ')' // method call
    ;
array:      '[' (expr ',')* expr? ']';
bool_type:  'true' | 'false';
import_stmt: 'import' '(' string ')';
string:     STRING;
if_stmt:    'if' '(' bool_expr ')' '{' top_level_stmt* '}' else_stmt?;
else_stmt:       'else' '{' top_level_stmt* '}';
bool_expr:  IDENT 
  | string
  | bool_expr '||' bool_expr 
  | bool_expr '&&' bool_expr 
  | '!' bool_expr
  | bool_expr '==' bool_expr
  | bool_expr '!=' bool_expr
  | '(' bool_expr ')'
  ;

INDEX : [0-9]+;
IDENT : [a-zA-Z_][a-zA-Z0-9_]*;
STRING : ["].*?["];
COMMENT : [#].*?[\n] -> skip;
WS : (' ' | '\t' | '\n' | '\r')+ -> skip;
