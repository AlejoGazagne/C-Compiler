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

NUMERO : DIGITO+ | DIGITO+'.'DIGITO+ ;

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
    | defFuncion
    | callFuncion PYC
    | prototipeFuncion PYC
    | bloque ;

declaracion : tdato ID definicion lista_var;

definicion : EQ opal 
    |
    ;

asignacion : ID EQ opal; //ver

bloque : LLA instrucciones LLC ;

retornar : RETURN opal;

lista_var : COMA ID definicion lista_var
    | 
    ;

while_stmt : WHILE PA opal PC instruccion;

if_stmt : IF PA opal PC instruccion
    | IF PA opal PC instruccion else_stmt;

else_stmt : ELSE bloque;

for_stmt : FOR PA asignacion PYC opal PYC asignacion PC instruccion;

opal : expresionl;

expresionl : terminol expl;

expl : ORR terminol expl
     |
     ;

terminol : expresion terml 
    | expresion log expresion terml;
    
terml : AND expresionl terml
      |
      ;

expresion : termino exp;

exp : MAS   termino exp
    | MENOS termino exp
    |
    ;

termino : factor term ;

term : MUL factor term
     | DIV factor term    
     | MOD factor term
     |
     ;

factor : ID
       | NUMERO
       | callFuncion
       | MENOS NUMERO
       | MENOS ID
       | PA expresionl PC
       ;

prototipeFuncion: tdato ID PA argProt PC ;
callFuncion: ID PA argEnv PC;
defFuncion: tdato ID PA argRec PC bloque;

argRec: tdato ID listaArgRec
    |
    ;

listaArgRec: COMA tdato ID listaArgRec
    |
    ;

argEnv: expresion listaArgEnv
    |
    ;

listaArgEnv: COMA expresion listaArgEnv
    | 
    ;

argProt: tdato ID listArgProt
    |
    ;
    
listArgProt: COMA tdato ID listArgProt
    |
    ;