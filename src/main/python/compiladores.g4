grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

EQ : '=' ;
PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
COMA : ',' ;

MAS : '+';
MENOS : '-';
MOD : '%';
MUL : '*';
DIV : '/';

LT: '<';
GT: '>';
LE: '<='; 
GE: '>=';
EQQ: '==';
NEQ: '!=';

AND: '&&';
ORR: '||';

log : LT | GT | LE | GE | EQQ | NEQ;

NUMERO : DIGITO+ ;

INT : 'int';
DOUBLE : 'double';
tdato: INT | DOUBLE;

WHILE : 'while' ;
IF : 'if';
ELSE : 'else';
FOR : 'for';
RETURN : 'return';

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\r\n] -> skip ;
OTRO : . ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
    | 
    ;

instruccion : declaracion PYC
    | asignacion PYC
    | retornar PYC
    | if_stmt
    | for_stmt
    | while_stmt
    | defFuncion PYC
    | callFuncion PYC
    | prototipeFuncion PYC
    | bloque ;

declaracion : tdato ID definicion lista_var;

definicion : EQ opar //ver
    |
    ;

asignacion : ID EQ oplo; //ver

bloque : LLA instrucciones LLC ;

retornar : RETURN ID
    | RETURN NUMERO
    | RETURN asignacion
    | RETURN declaracion;

lista_var : COMA ID definicion lista_var
    | 
    ;

while_stmt : WHILE PA oplo PC instruccion;

if_stmt : IF PA oplo PC instruccion
    | IF PA oplo PC instruccion else_stmt;

else_stmt : ELSE bloque;

for_stmt : FOR PA asignacion PYC oplo PYC asignacion PC instruccion;

opar: expresion;

expresion: termino exp;

exp: MAS termino exp
    | MENOS termino exp
    | 
    ;

termino: factor term;

term: MUL factor term
    | DIV factor term
    | MOD factor term
    | 
    ;

factor: NUMERO
    | ID
    | MENOS NUMERO
    | MENOS ID
    | callFuncion
    | PA expresion PC;

oplo: expresionLo;

expresionLo: terminoLo expLo;

expLo: ORR terminoLo expLo
    |
    ;

terminoLo: factorLo termLo;

termLo: AND factorLo termLo
    |
    ;

factorLo: factor 
    | comp 
    | PA expresionLo PC;

comp: opar log opar
    | comp log comp;

prototipeFuncion: tdato ID PA parRec PC ;
callFuncion: ID PA parEnv PC;
defFuncion: tdato ID PA parRec PC bloque;

listaParEnv: COMA expresion listaParEnv
    | 
    ;

parEnv: expresion listaParEnv
    |
    ;

listaParRec: COMA tdato ID listaParRec
    |
    ;

parRec: tdato ID listaParRec
    |
    ;