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

ST: '<';
GT: '>';
EQQ: '==';
DIFF: '!=';

AND: '&&';
OR: '||';

M1: ID+ '++';
D1 : ID+ '--';
M11 : '++'ID+; 
D11 : '--'ID+; 

log : ST | GT | EQQ | DIFF;
update : M1 | M11 | D1 | D11; 

NUMERO : DIGITO+ ;

TDATO : 'int' | 'double' ;
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
    | ;

instruccion : declaracion PYC
    | asignacion PYC
    | retornar PYC
    | if_stmt
    | for_stmt
    | while_stmt
    | bloque ;

declaracion : TDATO ID definicion lista_var;

definicion : (EQ NUMERO) 
    | ;

asignacion : (ID EQ NUMERO)
    | (ID EQ ID);

bloque : LLA instrucciones LLC ;

retornar : RETURN ID
    | RETURN NUMERO
    | RETURN asignacion
    | RETURN declaracion;

lista_var : COMA ID definicion lista_var
    | ;

while_stmt : WHILE PA opal PC instruccion;

if_stmt : IF PA opal PC instruccion
    | IF PA opal PC instruccion else_stmt;

else_stmt : ELSE bloque;

for_stmt : FOR PA (declaracion | asignacion) PYC opal PYC update PC instruccion;

opal : (ID log ID | ID log NUMERO | NUMERO log ID | NUMERO log NUMERO)
    | (ID log ID | ID log NUMERO | NUMERO log ID | NUMERO log NUMERO) AND opal;
// opal : comp 
//     | comp AND opal 
//     | comp OR opal;

// comp : ID log ID
//     | ID log NUMERO
//     | NUMERO log NUMERO
//     | NUMERO log ID;