grammar Decaf;

/*
 * Lexer Rules
 */
fragment ALPHA: [a-zA-Z_];

fragment DIGIT: [0-9];

fragment ALPHA_NUM: ALPHA | DIGIT;

fragment LETTER: [a-zA-Z];

ID: ALPHA ALPHA_NUM*;

NUM: DIGIT DIGIT*;

APOSTROPHE: '\'';

CHAR_LITERAL: APOSTROPHE (LETTER | [\\\t\n]) APOSTROPHE;

TRUE: 'true';

FALSE: 'false';

/*
 * Parser Rules
 */

program: 'class' 'Program' '{' (declaration)* '}';

declaration:
	structDeclaration
	| varDeclaration
	| methodDeclaration;

varDeclaration: varType ID ';' | varType ID '[' NUM ']' ';';

structDeclaration: 'struct' ID '{' (varDeclaration)* '}';

varType:
	'int'
	| 'char'
	| 'boolean'
	| 'struct' ID
	| structDeclaration
	| 'void';

methodDeclaration: methodType ID '(' (parameter)* ')' block;

methodType: 'int' | 'char' | 'boolean' | 'void';

parameter: parameterType ID | parameterType ID '[' ']';

parameterType: 'int' | 'char' | 'boolean';

block: '{' (varDeclaration)* (statement)* '}';

statement:
	'if' '(' expression ')' block ('else' block)?
	| 'while' '(' expression ')' block
	| 'return' expression? ';'
	| methodCall ';'
	| block
	| location '=' expression
	| expression? ';';

location: (ID | ID '[' expression ']') ('.' location)?;

expression:
	location
	| methodCall
	| literal
	| expression op expression
	| '-' expression
	| '!' expression
	| '(' expression ')';

methodCall: ID '(' arg* ')';

arg: expression;

op: arith_op | rel_op | eq_op | cond_op;

arith_op: '+' | '-' | '*' | '/' | '%';

rel_op: '<' | '>' | '<=' | '>=';

eq_op: '==' | '!=';

cond_op: '&&' | '||';

literal: int_literal | char_literal | bool_literal;

int_literal: NUM;

char_literal: '\'' CHAR_LITERAL '\'';

bool_literal: TRUE | FALSE;

WHITESPACE: [\t\r\n ] -> skip;