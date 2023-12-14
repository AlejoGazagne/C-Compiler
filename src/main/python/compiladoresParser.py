# Generated from /home/alejo/Escritorio/raviol/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
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
        4,1,31,302,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,80,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,112,
        8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,131,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,152,
        8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,177,
        8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,187,8,18,1,19,
        1,19,1,19,1,19,1,19,3,19,194,8,19,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,208,8,21,1,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        226,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,239,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        3,28,264,8,28,1,29,1,29,1,29,1,29,1,29,1,29,3,29,272,8,29,1,30,1,
        30,1,30,1,30,3,30,278,8,30,1,31,1,31,1,31,1,31,1,31,3,31,285,8,31,
        1,32,1,32,1,32,1,32,1,32,3,32,292,8,32,1,33,1,33,1,33,1,33,1,33,
        1,33,3,33,300,8,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,
        2,1,0,13,18,1,0,22,23,299,0,68,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,
        6,79,1,0,0,0,8,101,1,0,0,0,10,103,1,0,0,0,12,111,1,0,0,0,14,113,
        1,0,0,0,16,117,1,0,0,0,18,121,1,0,0,0,20,130,1,0,0,0,22,132,1,0,
        0,0,24,151,1,0,0,0,26,153,1,0,0,0,28,156,1,0,0,0,30,166,1,0,0,0,
        32,168,1,0,0,0,34,176,1,0,0,0,36,186,1,0,0,0,38,193,1,0,0,0,40,195,
        1,0,0,0,42,207,1,0,0,0,44,209,1,0,0,0,46,225,1,0,0,0,48,238,1,0,
        0,0,50,240,1,0,0,0,52,246,1,0,0,0,54,251,1,0,0,0,56,263,1,0,0,0,
        58,271,1,0,0,0,60,277,1,0,0,0,62,284,1,0,0,0,64,291,1,0,0,0,66,299,
        1,0,0,0,68,69,7,0,0,0,69,1,1,0,0,0,70,71,7,1,0,0,71,3,1,0,0,0,72,
        73,3,6,3,0,73,74,5,0,0,1,74,5,1,0,0,0,75,76,3,8,4,0,76,77,3,6,3,
        0,77,80,1,0,0,0,78,80,1,0,0,0,79,75,1,0,0,0,79,78,1,0,0,0,80,7,1,
        0,0,0,81,82,3,10,5,0,82,83,5,6,0,0,83,102,1,0,0,0,84,85,3,14,7,0,
        85,86,5,6,0,0,86,102,1,0,0,0,87,88,3,18,9,0,88,89,5,6,0,0,89,102,
        1,0,0,0,90,102,3,24,12,0,91,102,3,28,14,0,92,102,3,22,11,0,93,102,
        3,54,27,0,94,95,3,52,26,0,95,96,5,6,0,0,96,102,1,0,0,0,97,98,3,50,
        25,0,98,99,5,6,0,0,99,102,1,0,0,0,100,102,3,16,8,0,101,81,1,0,0,
        0,101,84,1,0,0,0,101,87,1,0,0,0,101,90,1,0,0,0,101,91,1,0,0,0,101,
        92,1,0,0,0,101,93,1,0,0,0,101,94,1,0,0,0,101,97,1,0,0,0,101,100,
        1,0,0,0,102,9,1,0,0,0,103,104,3,2,1,0,104,105,5,29,0,0,105,106,3,
        12,6,0,106,107,3,20,10,0,107,11,1,0,0,0,108,109,5,1,0,0,109,112,
        3,30,15,0,110,112,1,0,0,0,111,108,1,0,0,0,111,110,1,0,0,0,112,13,
        1,0,0,0,113,114,5,29,0,0,114,115,5,1,0,0,115,116,3,30,15,0,116,15,
        1,0,0,0,117,118,5,4,0,0,118,119,3,6,3,0,119,120,5,5,0,0,120,17,1,
        0,0,0,121,122,5,28,0,0,122,123,3,30,15,0,123,19,1,0,0,0,124,125,
        5,7,0,0,125,126,5,29,0,0,126,127,3,12,6,0,127,128,3,20,10,0,128,
        131,1,0,0,0,129,131,1,0,0,0,130,124,1,0,0,0,130,129,1,0,0,0,131,
        21,1,0,0,0,132,133,5,24,0,0,133,134,5,2,0,0,134,135,3,30,15,0,135,
        136,5,3,0,0,136,137,3,8,4,0,137,23,1,0,0,0,138,139,5,25,0,0,139,
        140,5,2,0,0,140,141,3,30,15,0,141,142,5,3,0,0,142,143,3,8,4,0,143,
        152,1,0,0,0,144,145,5,25,0,0,145,146,5,2,0,0,146,147,3,30,15,0,147,
        148,5,3,0,0,148,149,3,8,4,0,149,150,3,26,13,0,150,152,1,0,0,0,151,
        138,1,0,0,0,151,144,1,0,0,0,152,25,1,0,0,0,153,154,5,26,0,0,154,
        155,3,16,8,0,155,27,1,0,0,0,156,157,5,27,0,0,157,158,5,2,0,0,158,
        159,3,14,7,0,159,160,5,6,0,0,160,161,3,30,15,0,161,162,5,6,0,0,162,
        163,3,14,7,0,163,164,5,3,0,0,164,165,3,8,4,0,165,29,1,0,0,0,166,
        167,3,32,16,0,167,31,1,0,0,0,168,169,3,36,18,0,169,170,3,34,17,0,
        170,33,1,0,0,0,171,172,5,20,0,0,172,173,3,36,18,0,173,174,3,34,17,
        0,174,177,1,0,0,0,175,177,1,0,0,0,176,171,1,0,0,0,176,175,1,0,0,
        0,177,35,1,0,0,0,178,179,3,40,20,0,179,180,3,38,19,0,180,187,1,0,
        0,0,181,182,3,40,20,0,182,183,3,0,0,0,183,184,3,40,20,0,184,185,
        3,38,19,0,185,187,1,0,0,0,186,178,1,0,0,0,186,181,1,0,0,0,187,37,
        1,0,0,0,188,189,5,19,0,0,189,190,3,32,16,0,190,191,3,38,19,0,191,
        194,1,0,0,0,192,194,1,0,0,0,193,188,1,0,0,0,193,192,1,0,0,0,194,
        39,1,0,0,0,195,196,3,44,22,0,196,197,3,42,21,0,197,41,1,0,0,0,198,
        199,5,8,0,0,199,200,3,44,22,0,200,201,3,42,21,0,201,208,1,0,0,0,
        202,203,5,9,0,0,203,204,3,44,22,0,204,205,3,42,21,0,205,208,1,0,
        0,0,206,208,1,0,0,0,207,198,1,0,0,0,207,202,1,0,0,0,207,206,1,0,
        0,0,208,43,1,0,0,0,209,210,3,48,24,0,210,211,3,46,23,0,211,45,1,
        0,0,0,212,213,5,11,0,0,213,214,3,48,24,0,214,215,3,46,23,0,215,226,
        1,0,0,0,216,217,5,12,0,0,217,218,3,48,24,0,218,219,3,46,23,0,219,
        226,1,0,0,0,220,221,5,10,0,0,221,222,3,48,24,0,222,223,3,46,23,0,
        223,226,1,0,0,0,224,226,1,0,0,0,225,212,1,0,0,0,225,216,1,0,0,0,
        225,220,1,0,0,0,225,224,1,0,0,0,226,47,1,0,0,0,227,239,5,29,0,0,
        228,239,5,21,0,0,229,239,3,52,26,0,230,231,5,9,0,0,231,239,5,21,
        0,0,232,233,5,9,0,0,233,239,5,29,0,0,234,235,5,2,0,0,235,236,3,32,
        16,0,236,237,5,3,0,0,237,239,1,0,0,0,238,227,1,0,0,0,238,228,1,0,
        0,0,238,229,1,0,0,0,238,230,1,0,0,0,238,232,1,0,0,0,238,234,1,0,
        0,0,239,49,1,0,0,0,240,241,3,2,1,0,241,242,5,29,0,0,242,243,5,2,
        0,0,243,244,3,64,32,0,244,245,5,3,0,0,245,51,1,0,0,0,246,247,5,29,
        0,0,247,248,5,2,0,0,248,249,3,60,30,0,249,250,5,3,0,0,250,53,1,0,
        0,0,251,252,3,2,1,0,252,253,5,29,0,0,253,254,5,2,0,0,254,255,3,56,
        28,0,255,256,5,3,0,0,256,257,3,16,8,0,257,55,1,0,0,0,258,259,3,2,
        1,0,259,260,5,29,0,0,260,261,3,58,29,0,261,264,1,0,0,0,262,264,1,
        0,0,0,263,258,1,0,0,0,263,262,1,0,0,0,264,57,1,0,0,0,265,266,5,7,
        0,0,266,267,3,2,1,0,267,268,5,29,0,0,268,269,3,58,29,0,269,272,1,
        0,0,0,270,272,1,0,0,0,271,265,1,0,0,0,271,270,1,0,0,0,272,59,1,0,
        0,0,273,274,3,40,20,0,274,275,3,62,31,0,275,278,1,0,0,0,276,278,
        1,0,0,0,277,273,1,0,0,0,277,276,1,0,0,0,278,61,1,0,0,0,279,280,5,
        7,0,0,280,281,3,40,20,0,281,282,3,62,31,0,282,285,1,0,0,0,283,285,
        1,0,0,0,284,279,1,0,0,0,284,283,1,0,0,0,285,63,1,0,0,0,286,287,3,
        2,1,0,287,288,5,29,0,0,288,289,3,66,33,0,289,292,1,0,0,0,290,292,
        1,0,0,0,291,286,1,0,0,0,291,290,1,0,0,0,292,65,1,0,0,0,293,294,5,
        7,0,0,294,295,3,2,1,0,295,296,5,29,0,0,296,297,3,66,33,0,297,300,
        1,0,0,0,298,300,1,0,0,0,299,293,1,0,0,0,299,298,1,0,0,0,300,67,1,
        0,0,0,17,79,101,111,130,151,176,186,193,207,225,238,263,271,277,
        284,291,299
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", "';'", 
                     "','", "'+'", "'-'", "'%'", "'*'", "'/'", "'<'", "'>'", 
                     "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", "<INVALID>", 
                     "'int'", "'double'", "'while'", "'if'", "'else'", "'for'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "EQ", "PA", "PC", "LLA", "LLC", "PYC", 
                      "COMA", "MAS", "MENOS", "MOD", "MUL", "DIV", "LT", 
                      "GT", "LE", "GE", "EQQ", "NEQ", "AND", "ORR", "NUMERO", 
                      "INT", "DOUBLE", "WHILE", "IF", "ELSE", "FOR", "RETURN", 
                      "ID", "WS", "OTRO" ]

    RULE_log = 0
    RULE_tdato = 1
    RULE_programa = 2
    RULE_instrucciones = 3
    RULE_instruccion = 4
    RULE_declaracion = 5
    RULE_definicion = 6
    RULE_asignacion = 7
    RULE_bloque = 8
    RULE_retornar = 9
    RULE_lista_var = 10
    RULE_while_stmt = 11
    RULE_if_stmt = 12
    RULE_else_stmt = 13
    RULE_for_stmt = 14
    RULE_opal = 15
    RULE_expresionl = 16
    RULE_expl = 17
    RULE_terminol = 18
    RULE_terml = 19
    RULE_expresion = 20
    RULE_exp = 21
    RULE_termino = 22
    RULE_term = 23
    RULE_factor = 24
    RULE_prototipeFuncion = 25
    RULE_callFuncion = 26
    RULE_defFuncion = 27
    RULE_argRec = 28
    RULE_listaArgRec = 29
    RULE_argEnv = 30
    RULE_listaArgEnv = 31
    RULE_argProt = 32
    RULE_listArgProt = 33

    ruleNames =  [ "log", "tdato", "programa", "instrucciones", "instruccion", 
                   "declaracion", "definicion", "asignacion", "bloque", 
                   "retornar", "lista_var", "while_stmt", "if_stmt", "else_stmt", 
                   "for_stmt", "opal", "expresionl", "expl", "terminol", 
                   "terml", "expresion", "exp", "termino", "term", "factor", 
                   "prototipeFuncion", "callFuncion", "defFuncion", "argRec", 
                   "listaArgRec", "argEnv", "listaArgEnv", "argProt", "listArgProt" ]

    EOF = Token.EOF
    EQ=1
    PA=2
    PC=3
    LLA=4
    LLC=5
    PYC=6
    COMA=7
    MAS=8
    MENOS=9
    MOD=10
    MUL=11
    DIV=12
    LT=13
    GT=14
    LE=15
    GE=16
    EQQ=17
    NEQ=18
    AND=19
    ORR=20
    NUMERO=21
    INT=22
    DOUBLE=23
    WHILE=24
    IF=25
    ELSE=26
    FOR=27
    RETURN=28
    ID=29
    WS=30
    OTRO=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(compiladoresParser.LT, 0)

        def GT(self):
            return self.getToken(compiladoresParser.GT, 0)

        def LE(self):
            return self.getToken(compiladoresParser.LE, 0)

        def GE(self):
            return self.getToken(compiladoresParser.GE, 0)

        def EQQ(self):
            return self.getToken(compiladoresParser.EQQ, 0)

        def NEQ(self):
            return self.getToken(compiladoresParser.NEQ, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog" ):
                return visitor.visitLog(self)
            else:
                return visitor.visitChildren(self)




    def log(self):

        localctx = compiladoresParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_log)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
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


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tdato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.instrucciones()
            self.state = 73
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instrucciones)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 22, 23, 24, 25, 27, 28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.instruccion()
                self.state = 76
                self.instrucciones()
                pass
            elif token in [-1, 5]:
                self.enterOuterAlt(localctx, 2)

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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def retornar(self):
            return self.getTypedRuleContext(compiladoresParser.RetornarContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.While_stmtContext,0)


        def defFuncion(self):
            return self.getTypedRuleContext(compiladoresParser.DefFuncionContext,0)


        def callFuncion(self):
            return self.getTypedRuleContext(compiladoresParser.CallFuncionContext,0)


        def prototipeFuncion(self):
            return self.getTypedRuleContext(compiladoresParser.PrototipeFuncionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruccion)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.declaracion()
                self.state = 82
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.asignacion()
                self.state = 85
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.retornar()
                self.state = 88
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.defFuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.callFuncion()
                self.state = 95
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.prototipeFuncion()
                self.state = 98
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 100
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def definicion(self):
            return self.getTypedRuleContext(compiladoresParser.DefinicionContext,0)


        def lista_var(self):
            return self.getTypedRuleContext(compiladoresParser.Lista_varContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.tdato()
            self.state = 104
            self.match(compiladoresParser.ID)
            self.state = 105
            self.definicion()
            self.state = 106
            self.lista_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(compiladoresParser.EQ, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_definicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicion" ):
                listener.enterDefinicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicion" ):
                listener.exitDefinicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicion" ):
                return visitor.visitDefinicion(self)
            else:
                return visitor.visitChildren(self)




    def definicion(self):

        localctx = compiladoresParser.DefinicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_definicion)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(compiladoresParser.EQ)
                self.state = 109
                self.opal()
                pass
            elif token in [6, 7]:
                self.enterOuterAlt(localctx, 2)

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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def EQ(self):
            return self.getToken(compiladoresParser.EQ, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(compiladoresParser.ID)
            self.state = 114
            self.match(compiladoresParser.EQ)
            self.state = 115
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(compiladoresParser.LLA)
            self.state = 118
            self.instrucciones()
            self.state = 119
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_retornar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornar" ):
                listener.enterRetornar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornar" ):
                listener.exitRetornar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetornar" ):
                return visitor.visitRetornar(self)
            else:
                return visitor.visitChildren(self)




    def retornar(self):

        localctx = compiladoresParser.RetornarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_retornar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(compiladoresParser.RETURN)
            self.state = 122
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def definicion(self):
            return self.getTypedRuleContext(compiladoresParser.DefinicionContext,0)


        def lista_var(self):
            return self.getTypedRuleContext(compiladoresParser.Lista_varContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lista_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_var" ):
                listener.enterLista_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_var" ):
                listener.exitLista_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_var" ):
                return visitor.visitLista_var(self)
            else:
                return visitor.visitChildren(self)




    def lista_var(self):

        localctx = compiladoresParser.Lista_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_lista_var)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(compiladoresParser.COMA)
                self.state = 125
                self.match(compiladoresParser.ID)
                self.state = 126
                self.definicion()
                self.state = 127
                self.lista_var()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

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


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = compiladoresParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(compiladoresParser.WHILE)
            self.state = 133
            self.match(compiladoresParser.PA)
            self.state = 134
            self.opal()
            self.state = 135
            self.match(compiladoresParser.PC)
            self.state = 136
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(compiladoresParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = compiladoresParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(compiladoresParser.IF)
                self.state = 139
                self.match(compiladoresParser.PA)
                self.state = 140
                self.opal()
                self.state = 141
                self.match(compiladoresParser.PC)
                self.state = 142
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(compiladoresParser.IF)
                self.state = 145
                self.match(compiladoresParser.PA)
                self.state = 146
                self.opal()
                self.state = 147
                self.match(compiladoresParser.PC)
                self.state = 148
                self.instruccion()
                self.state = 149
                self.else_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_else_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = compiladoresParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(compiladoresParser.ELSE)
            self.state = 154
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.AsignacionContext,i)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = compiladoresParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(compiladoresParser.FOR)
            self.state = 157
            self.match(compiladoresParser.PA)
            self.state = 158
            self.asignacion()
            self.state = 159
            self.match(compiladoresParser.PYC)
            self.state = 160
            self.opal()
            self.state = 161
            self.match(compiladoresParser.PYC)
            self.state = 162
            self.asignacion()
            self.state = 163
            self.match(compiladoresParser.PC)
            self.state = 164
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionl(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionlContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expresionl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminol(self):
            return self.getTypedRuleContext(compiladoresParser.TerminolContext,0)


        def expl(self):
            return self.getTypedRuleContext(compiladoresParser.ExplContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_expresionl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionl" ):
                listener.enterExpresionl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionl" ):
                listener.exitExpresionl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionl" ):
                return visitor.visitExpresionl(self)
            else:
                return visitor.visitChildren(self)




    def expresionl(self):

        localctx = compiladoresParser.ExpresionlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expresionl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.terminol()
            self.state = 169
            self.expl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORR(self):
            return self.getToken(compiladoresParser.ORR, 0)

        def terminol(self):
            return self.getTypedRuleContext(compiladoresParser.TerminolContext,0)


        def expl(self):
            return self.getTypedRuleContext(compiladoresParser.ExplContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_expl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpl" ):
                listener.enterExpl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpl" ):
                listener.exitExpl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpl" ):
                return visitor.visitExpl(self)
            else:
                return visitor.visitChildren(self)




    def expl(self):

        localctx = compiladoresParser.ExplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expl)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(compiladoresParser.ORR)
                self.state = 172
                self.terminol()
                self.state = 173
                self.expl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpresionContext,i)


        def terml(self):
            return self.getTypedRuleContext(compiladoresParser.TermlContext,0)


        def log(self):
            return self.getTypedRuleContext(compiladoresParser.LogContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_terminol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminol" ):
                listener.enterTerminol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminol" ):
                listener.exitTerminol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminol" ):
                return visitor.visitTerminol(self)
            else:
                return visitor.visitChildren(self)




    def terminol(self):

        localctx = compiladoresParser.TerminolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_terminol)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.expresion()
                self.state = 179
                self.terml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.expresion()
                self.state = 182
                self.log()
                self.state = 183
                self.expresion()
                self.state = 184
                self.terml()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def expresionl(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionlContext,0)


        def terml(self):
            return self.getTypedRuleContext(compiladoresParser.TermlContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_terml

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerml" ):
                listener.enterTerml(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerml" ):
                listener.exitTerml(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerml" ):
                return visitor.visitTerml(self)
            else:
                return visitor.visitChildren(self)




    def terml(self):

        localctx = compiladoresParser.TermlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_terml)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(compiladoresParser.AND)
                self.state = 189
                self.expresionl()
                self.state = 190
                self.terml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(compiladoresParser.TerminoContext,0)


        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = compiladoresParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.termino()
            self.state = 196
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(compiladoresParser.MAS, 0)

        def termino(self):
            return self.getTypedRuleContext(compiladoresParser.TerminoContext,0)


        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def MENOS(self):
            return self.getToken(compiladoresParser.MENOS, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(compiladoresParser.MAS)
                self.state = 199
                self.termino()
                self.state = 200
                self.exp()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(compiladoresParser.MENOS)
                self.state = 203
                self.termino()
                self.state = 204
                self.exp()
                pass
            elif token in [3, 6, 7, 13, 14, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 3)

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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = compiladoresParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.factor()
            self.state = 210
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(compiladoresParser.MUL, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_term)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(compiladoresParser.MUL)
                self.state = 213
                self.factor()
                self.state = 214
                self.term()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(compiladoresParser.DIV)
                self.state = 217
                self.factor()
                self.state = 218
                self.term()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(compiladoresParser.MOD)
                self.state = 221
                self.factor()
                self.state = 222
                self.term()
                pass
            elif token in [3, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 4)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def callFuncion(self):
            return self.getTypedRuleContext(compiladoresParser.CallFuncionContext,0)


        def MENOS(self):
            return self.getToken(compiladoresParser.MENOS, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def expresionl(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionlContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_factor)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.callFuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
                self.match(compiladoresParser.MENOS)
                self.state = 231
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.match(compiladoresParser.MENOS)
                self.state = 233
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.match(compiladoresParser.PA)
                self.state = 235
                self.expresionl()
                self.state = 236
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototipeFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argProt(self):
            return self.getTypedRuleContext(compiladoresParser.ArgProtContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_prototipeFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipeFuncion" ):
                listener.enterPrototipeFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipeFuncion" ):
                listener.exitPrototipeFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipeFuncion" ):
                return visitor.visitPrototipeFuncion(self)
            else:
                return visitor.visitChildren(self)




    def prototipeFuncion(self):

        localctx = compiladoresParser.PrototipeFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_prototipeFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.tdato()
            self.state = 241
            self.match(compiladoresParser.ID)
            self.state = 242
            self.match(compiladoresParser.PA)
            self.state = 243
            self.argProt()
            self.state = 244
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ArgEnvContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_callFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFuncion" ):
                listener.enterCallFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFuncion" ):
                listener.exitCallFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFuncion" ):
                return visitor.visitCallFuncion(self)
            else:
                return visitor.visitChildren(self)




    def callFuncion(self):

        localctx = compiladoresParser.CallFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_callFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(compiladoresParser.ID)
            self.state = 247
            self.match(compiladoresParser.PA)
            self.state = 248
            self.argEnv()
            self.state = 249
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argRec(self):
            return self.getTypedRuleContext(compiladoresParser.ArgRecContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_defFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefFuncion" ):
                listener.enterDefFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefFuncion" ):
                listener.exitDefFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefFuncion" ):
                return visitor.visitDefFuncion(self)
            else:
                return visitor.visitChildren(self)




    def defFuncion(self):

        localctx = compiladoresParser.DefFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_defFuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.tdato()
            self.state = 252
            self.match(compiladoresParser.ID)
            self.state = 253
            self.match(compiladoresParser.PA)
            self.state = 254
            self.argRec()
            self.state = 255
            self.match(compiladoresParser.PC)
            self.state = 256
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgRecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def listaArgRec(self):
            return self.getTypedRuleContext(compiladoresParser.ListaArgRecContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argRec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgRec" ):
                listener.enterArgRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgRec" ):
                listener.exitArgRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgRec" ):
                return visitor.visitArgRec(self)
            else:
                return visitor.visitChildren(self)




    def argRec(self):

        localctx = compiladoresParser.ArgRecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_argRec)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.tdato()
                self.state = 259
                self.match(compiladoresParser.ID)
                self.state = 260
                self.listaArgRec()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaArgRecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def listaArgRec(self):
            return self.getTypedRuleContext(compiladoresParser.ListaArgRecContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_listaArgRec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgRec" ):
                listener.enterListaArgRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgRec" ):
                listener.exitListaArgRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgRec" ):
                return visitor.visitListaArgRec(self)
            else:
                return visitor.visitChildren(self)




    def listaArgRec(self):

        localctx = compiladoresParser.ListaArgRecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_listaArgRec)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(compiladoresParser.COMA)
                self.state = 266
                self.tdato()
                self.state = 267
                self.match(compiladoresParser.ID)
                self.state = 268
                self.listaArgRec()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgEnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionContext,0)


        def listaArgEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ListaArgEnvContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argEnv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgEnv" ):
                listener.enterArgEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgEnv" ):
                listener.exitArgEnv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgEnv" ):
                return visitor.visitArgEnv(self)
            else:
                return visitor.visitChildren(self)




    def argEnv(self):

        localctx = compiladoresParser.ArgEnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argEnv)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 9, 21, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.expresion()
                self.state = 274
                self.listaArgEnv()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaArgEnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionContext,0)


        def listaArgEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ListaArgEnvContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_listaArgEnv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgEnv" ):
                listener.enterListaArgEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgEnv" ):
                listener.exitListaArgEnv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgEnv" ):
                return visitor.visitListaArgEnv(self)
            else:
                return visitor.visitChildren(self)




    def listaArgEnv(self):

        localctx = compiladoresParser.ListaArgEnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_listaArgEnv)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(compiladoresParser.COMA)
                self.state = 280
                self.expresion()
                self.state = 281
                self.listaArgEnv()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgProtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def listArgProt(self):
            return self.getTypedRuleContext(compiladoresParser.ListArgProtContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argProt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgProt" ):
                listener.enterArgProt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgProt" ):
                listener.exitArgProt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgProt" ):
                return visitor.visitArgProt(self)
            else:
                return visitor.visitChildren(self)




    def argProt(self):

        localctx = compiladoresParser.ArgProtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argProt)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.tdato()
                self.state = 287
                self.match(compiladoresParser.ID)
                self.state = 288
                self.listArgProt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class ListArgProtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def listArgProt(self):
            return self.getTypedRuleContext(compiladoresParser.ListArgProtContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_listArgProt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListArgProt" ):
                listener.enterListArgProt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListArgProt" ):
                listener.exitListArgProt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListArgProt" ):
                return visitor.visitListArgProt(self)
            else:
                return visitor.visitChildren(self)




    def listArgProt(self):

        localctx = compiladoresParser.ListArgProtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_listArgProt)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(compiladoresParser.COMA)
                self.state = 294
                self.tdato()
                self.state = 295
                self.match(compiladoresParser.ID)
                self.state = 296
                self.listArgProt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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





