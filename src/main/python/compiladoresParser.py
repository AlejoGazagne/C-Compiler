# Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
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
        4,1,31,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,1,1,
        1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,
        4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,108,8,6,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,126,8,9,1,10,1,
        10,1,10,1,10,1,10,1,10,3,10,134,8,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,155,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,3,17,180,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,190,
        8,18,1,19,1,19,1,19,1,19,1,19,3,19,197,8,19,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,211,8,21,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,229,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,242,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,28,3,28,267,8,28,1,29,1,29,1,29,1,29,3,29,273,8,29,1,30,1,
        30,1,30,1,30,1,30,1,30,3,30,281,8,30,1,31,1,31,1,31,1,31,1,31,3,
        31,288,8,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,2,1,0,13,18,
        1,0,22,23,290,0,64,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,75,1,0,0,
        0,8,97,1,0,0,0,10,99,1,0,0,0,12,107,1,0,0,0,14,109,1,0,0,0,16,113,
        1,0,0,0,18,125,1,0,0,0,20,133,1,0,0,0,22,135,1,0,0,0,24,154,1,0,
        0,0,26,156,1,0,0,0,28,159,1,0,0,0,30,169,1,0,0,0,32,171,1,0,0,0,
        34,179,1,0,0,0,36,189,1,0,0,0,38,196,1,0,0,0,40,198,1,0,0,0,42,210,
        1,0,0,0,44,212,1,0,0,0,46,228,1,0,0,0,48,241,1,0,0,0,50,243,1,0,
        0,0,52,249,1,0,0,0,54,254,1,0,0,0,56,266,1,0,0,0,58,272,1,0,0,0,
        60,280,1,0,0,0,62,287,1,0,0,0,64,65,7,0,0,0,65,1,1,0,0,0,66,67,7,
        1,0,0,67,3,1,0,0,0,68,69,3,6,3,0,69,70,5,0,0,1,70,5,1,0,0,0,71,72,
        3,8,4,0,72,73,3,6,3,0,73,76,1,0,0,0,74,76,1,0,0,0,75,71,1,0,0,0,
        75,74,1,0,0,0,76,7,1,0,0,0,77,78,3,10,5,0,78,79,5,6,0,0,79,98,1,
        0,0,0,80,81,3,14,7,0,81,82,5,6,0,0,82,98,1,0,0,0,83,84,3,18,9,0,
        84,85,5,6,0,0,85,98,1,0,0,0,86,98,3,24,12,0,87,98,3,28,14,0,88,98,
        3,22,11,0,89,98,3,54,27,0,90,91,3,52,26,0,91,92,5,6,0,0,92,98,1,
        0,0,0,93,94,3,50,25,0,94,95,5,6,0,0,95,98,1,0,0,0,96,98,3,16,8,0,
        97,77,1,0,0,0,97,80,1,0,0,0,97,83,1,0,0,0,97,86,1,0,0,0,97,87,1,
        0,0,0,97,88,1,0,0,0,97,89,1,0,0,0,97,90,1,0,0,0,97,93,1,0,0,0,97,
        96,1,0,0,0,98,9,1,0,0,0,99,100,3,2,1,0,100,101,5,29,0,0,101,102,
        3,12,6,0,102,103,3,20,10,0,103,11,1,0,0,0,104,105,5,1,0,0,105,108,
        3,30,15,0,106,108,1,0,0,0,107,104,1,0,0,0,107,106,1,0,0,0,108,13,
        1,0,0,0,109,110,5,29,0,0,110,111,5,1,0,0,111,112,3,30,15,0,112,15,
        1,0,0,0,113,114,5,4,0,0,114,115,3,6,3,0,115,116,5,5,0,0,116,17,1,
        0,0,0,117,118,5,28,0,0,118,126,5,29,0,0,119,120,5,28,0,0,120,126,
        5,21,0,0,121,122,5,28,0,0,122,126,3,14,7,0,123,124,5,28,0,0,124,
        126,3,10,5,0,125,117,1,0,0,0,125,119,1,0,0,0,125,121,1,0,0,0,125,
        123,1,0,0,0,126,19,1,0,0,0,127,128,5,7,0,0,128,129,5,29,0,0,129,
        130,3,12,6,0,130,131,3,20,10,0,131,134,1,0,0,0,132,134,1,0,0,0,133,
        127,1,0,0,0,133,132,1,0,0,0,134,21,1,0,0,0,135,136,5,24,0,0,136,
        137,5,2,0,0,137,138,3,30,15,0,138,139,5,3,0,0,139,140,3,8,4,0,140,
        23,1,0,0,0,141,142,5,25,0,0,142,143,5,2,0,0,143,144,3,30,15,0,144,
        145,5,3,0,0,145,146,3,8,4,0,146,155,1,0,0,0,147,148,5,25,0,0,148,
        149,5,2,0,0,149,150,3,30,15,0,150,151,5,3,0,0,151,152,3,8,4,0,152,
        153,3,26,13,0,153,155,1,0,0,0,154,141,1,0,0,0,154,147,1,0,0,0,155,
        25,1,0,0,0,156,157,5,26,0,0,157,158,3,16,8,0,158,27,1,0,0,0,159,
        160,5,27,0,0,160,161,5,2,0,0,161,162,3,14,7,0,162,163,5,6,0,0,163,
        164,3,30,15,0,164,165,5,6,0,0,165,166,3,14,7,0,166,167,5,3,0,0,167,
        168,3,8,4,0,168,29,1,0,0,0,169,170,3,32,16,0,170,31,1,0,0,0,171,
        172,3,36,18,0,172,173,3,34,17,0,173,33,1,0,0,0,174,175,5,20,0,0,
        175,176,3,36,18,0,176,177,3,34,17,0,177,180,1,0,0,0,178,180,1,0,
        0,0,179,174,1,0,0,0,179,178,1,0,0,0,180,35,1,0,0,0,181,182,3,40,
        20,0,182,183,3,38,19,0,183,190,1,0,0,0,184,185,3,40,20,0,185,186,
        3,0,0,0,186,187,3,40,20,0,187,188,3,38,19,0,188,190,1,0,0,0,189,
        181,1,0,0,0,189,184,1,0,0,0,190,37,1,0,0,0,191,192,5,19,0,0,192,
        193,3,32,16,0,193,194,3,38,19,0,194,197,1,0,0,0,195,197,1,0,0,0,
        196,191,1,0,0,0,196,195,1,0,0,0,197,39,1,0,0,0,198,199,3,44,22,0,
        199,200,3,42,21,0,200,41,1,0,0,0,201,202,5,8,0,0,202,203,3,44,22,
        0,203,204,3,42,21,0,204,211,1,0,0,0,205,206,5,9,0,0,206,207,3,44,
        22,0,207,208,3,42,21,0,208,211,1,0,0,0,209,211,1,0,0,0,210,201,1,
        0,0,0,210,205,1,0,0,0,210,209,1,0,0,0,211,43,1,0,0,0,212,213,3,48,
        24,0,213,214,3,46,23,0,214,45,1,0,0,0,215,216,5,11,0,0,216,217,3,
        48,24,0,217,218,3,46,23,0,218,229,1,0,0,0,219,220,5,12,0,0,220,221,
        3,48,24,0,221,222,3,46,23,0,222,229,1,0,0,0,223,224,5,10,0,0,224,
        225,3,48,24,0,225,226,3,46,23,0,226,229,1,0,0,0,227,229,1,0,0,0,
        228,215,1,0,0,0,228,219,1,0,0,0,228,223,1,0,0,0,228,227,1,0,0,0,
        229,47,1,0,0,0,230,242,5,29,0,0,231,242,5,21,0,0,232,242,3,52,26,
        0,233,234,5,9,0,0,234,242,5,21,0,0,235,236,5,9,0,0,236,242,5,29,
        0,0,237,238,5,2,0,0,238,239,3,32,16,0,239,240,5,3,0,0,240,242,1,
        0,0,0,241,230,1,0,0,0,241,231,1,0,0,0,241,232,1,0,0,0,241,233,1,
        0,0,0,241,235,1,0,0,0,241,237,1,0,0,0,242,49,1,0,0,0,243,244,3,2,
        1,0,244,245,5,29,0,0,245,246,5,2,0,0,246,247,3,62,31,0,247,248,5,
        3,0,0,248,51,1,0,0,0,249,250,5,29,0,0,250,251,5,2,0,0,251,252,3,
        58,29,0,252,253,5,3,0,0,253,53,1,0,0,0,254,255,3,2,1,0,255,256,5,
        29,0,0,256,257,5,2,0,0,257,258,3,62,31,0,258,259,5,3,0,0,259,260,
        3,16,8,0,260,55,1,0,0,0,261,262,5,7,0,0,262,263,3,40,20,0,263,264,
        3,56,28,0,264,267,1,0,0,0,265,267,1,0,0,0,266,261,1,0,0,0,266,265,
        1,0,0,0,267,57,1,0,0,0,268,269,3,40,20,0,269,270,3,56,28,0,270,273,
        1,0,0,0,271,273,1,0,0,0,272,268,1,0,0,0,272,271,1,0,0,0,273,59,1,
        0,0,0,274,275,5,7,0,0,275,276,3,2,1,0,276,277,5,29,0,0,277,278,3,
        60,30,0,278,281,1,0,0,0,279,281,1,0,0,0,280,274,1,0,0,0,280,279,
        1,0,0,0,281,61,1,0,0,0,282,283,3,2,1,0,283,284,5,29,0,0,284,285,
        3,60,30,0,285,288,1,0,0,0,286,288,1,0,0,0,287,282,1,0,0,0,287,286,
        1,0,0,0,288,63,1,0,0,0,16,75,97,107,125,133,154,179,189,196,210,
        228,241,266,272,280,287
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
    RULE_listaParEnv = 28
    RULE_parEnv = 29
    RULE_listaParRec = 30
    RULE_parRec = 31

    ruleNames =  [ "log", "tdato", "programa", "instrucciones", "instruccion", 
                   "declaracion", "definicion", "asignacion", "bloque", 
                   "retornar", "lista_var", "while_stmt", "if_stmt", "else_stmt", 
                   "for_stmt", "opal", "expresionl", "expl", "terminol", 
                   "terml", "expresion", "exp", "termino", "term", "factor", 
                   "prototipeFuncion", "callFuncion", "defFuncion", "listaParEnv", 
                   "parEnv", "listaParRec", "parRec" ]

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
            self.state = 64
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
            self.state = 66
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
            self.state = 68
            self.instrucciones()
            self.state = 69
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 22, 23, 24, 25, 27, 28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.instruccion()
                self.state = 72
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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.declaracion()
                self.state = 78
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.asignacion()
                self.state = 81
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.retornar()
                self.state = 84
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.defFuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.callFuncion()
                self.state = 91
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
                self.prototipeFuncion()
                self.state = 94
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 96
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
            self.state = 99
            self.tdato()
            self.state = 100
            self.match(compiladoresParser.ID)
            self.state = 101
            self.definicion()
            self.state = 102
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(compiladoresParser.EQ)
                self.state = 105
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
            self.state = 109
            self.match(compiladoresParser.ID)
            self.state = 110
            self.match(compiladoresParser.EQ)
            self.state = 111
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
            self.state = 113
            self.match(compiladoresParser.LLA)
            self.state = 114
            self.instrucciones()
            self.state = 115
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(compiladoresParser.RETURN)
                self.state = 118
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(compiladoresParser.RETURN)
                self.state = 120
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(compiladoresParser.RETURN)
                self.state = 122
                self.asignacion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(compiladoresParser.RETURN)
                self.state = 124
                self.declaracion()
                pass


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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(compiladoresParser.COMA)
                self.state = 128
                self.match(compiladoresParser.ID)
                self.state = 129
                self.definicion()
                self.state = 130
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
            self.state = 135
            self.match(compiladoresParser.WHILE)
            self.state = 136
            self.match(compiladoresParser.PA)
            self.state = 137
            self.opal()
            self.state = 138
            self.match(compiladoresParser.PC)
            self.state = 139
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(compiladoresParser.IF)
                self.state = 142
                self.match(compiladoresParser.PA)
                self.state = 143
                self.opal()
                self.state = 144
                self.match(compiladoresParser.PC)
                self.state = 145
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(compiladoresParser.IF)
                self.state = 148
                self.match(compiladoresParser.PA)
                self.state = 149
                self.opal()
                self.state = 150
                self.match(compiladoresParser.PC)
                self.state = 151
                self.instruccion()
                self.state = 152
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
            self.state = 156
            self.match(compiladoresParser.ELSE)
            self.state = 157
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
            self.state = 159
            self.match(compiladoresParser.FOR)
            self.state = 160
            self.match(compiladoresParser.PA)
            self.state = 161
            self.asignacion()
            self.state = 162
            self.match(compiladoresParser.PYC)
            self.state = 163
            self.opal()
            self.state = 164
            self.match(compiladoresParser.PYC)
            self.state = 165
            self.asignacion()
            self.state = 166
            self.match(compiladoresParser.PC)
            self.state = 167
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
            self.state = 169
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
            self.state = 171
            self.terminol()
            self.state = 172
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(compiladoresParser.ORR)
                self.state = 175
                self.terminol()
                self.state = 176
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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expresion()
                self.state = 182
                self.terml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.expresion()
                self.state = 185
                self.log()
                self.state = 186
                self.expresion()
                self.state = 187
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(compiladoresParser.AND)
                self.state = 192
                self.expresionl()
                self.state = 193
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
            self.state = 198
            self.termino()
            self.state = 199
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
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(compiladoresParser.MAS)
                self.state = 202
                self.termino()
                self.state = 203
                self.exp()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(compiladoresParser.MENOS)
                self.state = 206
                self.termino()
                self.state = 207
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
            self.state = 212
            self.factor()
            self.state = 213
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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(compiladoresParser.MUL)
                self.state = 216
                self.factor()
                self.state = 217
                self.term()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(compiladoresParser.DIV)
                self.state = 220
                self.factor()
                self.state = 221
                self.term()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(compiladoresParser.MOD)
                self.state = 224
                self.factor()
                self.state = 225
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
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.callFuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.match(compiladoresParser.MENOS)
                self.state = 234
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
                self.match(compiladoresParser.MENOS)
                self.state = 236
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.match(compiladoresParser.PA)
                self.state = 238
                self.expresionl()
                self.state = 239
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

        def parRec(self):
            return self.getTypedRuleContext(compiladoresParser.ParRecContext,0)


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
            self.state = 243
            self.tdato()
            self.state = 244
            self.match(compiladoresParser.ID)
            self.state = 245
            self.match(compiladoresParser.PA)
            self.state = 246
            self.parRec()
            self.state = 247
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

        def parEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ParEnvContext,0)


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
            self.state = 249
            self.match(compiladoresParser.ID)
            self.state = 250
            self.match(compiladoresParser.PA)
            self.state = 251
            self.parEnv()
            self.state = 252
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

        def parRec(self):
            return self.getTypedRuleContext(compiladoresParser.ParRecContext,0)


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
            self.state = 254
            self.tdato()
            self.state = 255
            self.match(compiladoresParser.ID)
            self.state = 256
            self.match(compiladoresParser.PA)
            self.state = 257
            self.parRec()
            self.state = 258
            self.match(compiladoresParser.PC)
            self.state = 259
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParEnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionContext,0)


        def listaParEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ListaParEnvContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_listaParEnv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParEnv" ):
                listener.enterListaParEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParEnv" ):
                listener.exitListaParEnv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParEnv" ):
                return visitor.visitListaParEnv(self)
            else:
                return visitor.visitChildren(self)




    def listaParEnv(self):

        localctx = compiladoresParser.ListaParEnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_listaParEnv)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(compiladoresParser.COMA)
                self.state = 262
                self.expresion()
                self.state = 263
                self.listaParEnv()
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


    class ParEnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(compiladoresParser.ExpresionContext,0)


        def listaParEnv(self):
            return self.getTypedRuleContext(compiladoresParser.ListaParEnvContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parEnv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParEnv" ):
                listener.enterParEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParEnv" ):
                listener.exitParEnv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParEnv" ):
                return visitor.visitParEnv(self)
            else:
                return visitor.visitChildren(self)




    def parEnv(self):

        localctx = compiladoresParser.ParEnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parEnv)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 9, 21, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.expresion()
                self.state = 269
                self.listaParEnv()
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


    class ListaParRecContext(ParserRuleContext):
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

        def listaParRec(self):
            return self.getTypedRuleContext(compiladoresParser.ListaParRecContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_listaParRec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParRec" ):
                listener.enterListaParRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParRec" ):
                listener.exitListaParRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParRec" ):
                return visitor.visitListaParRec(self)
            else:
                return visitor.visitChildren(self)




    def listaParRec(self):

        localctx = compiladoresParser.ListaParRecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_listaParRec)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(compiladoresParser.COMA)
                self.state = 275
                self.tdato()
                self.state = 276
                self.match(compiladoresParser.ID)
                self.state = 277
                self.listaParRec()
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


    class ParRecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def listaParRec(self):
            return self.getTypedRuleContext(compiladoresParser.ListaParRecContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parRec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParRec" ):
                listener.enterParRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParRec" ):
                listener.exitParRec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParRec" ):
                return visitor.visitParRec(self)
            else:
                return visitor.visitChildren(self)




    def parRec(self):

        localctx = compiladoresParser.ParRecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parRec)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.tdato()
                self.state = 283
                self.match(compiladoresParser.ID)
                self.state = 284
                self.listaParRec()
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





