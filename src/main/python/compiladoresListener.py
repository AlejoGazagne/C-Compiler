# Generated from /home/alejo/Escritorio/Aritmeticas y logicas andando/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#log.
    def enterLog(self, ctx:compiladoresParser.LogContext):
        pass

    # Exit a parse tree produced by compiladoresParser#log.
    def exitLog(self, ctx:compiladoresParser.LogContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tdato.
    def enterTdato(self, ctx:compiladoresParser.TdatoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tdato.
    def exitTdato(self, ctx:compiladoresParser.TdatoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#definicion.
    def enterDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#definicion.
    def exitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#retornar.
    def enterRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retornar.
    def exitRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_var.
    def enterLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_var.
    def exitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass


    # Enter a parse tree produced by compiladoresParser#while_stmt.
    def enterWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#while_stmt.
    def exitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#if_stmt.
    def enterIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#if_stmt.
    def exitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#else_stmt.
    def enterElse_stmt(self, ctx:compiladoresParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#else_stmt.
    def exitElse_stmt(self, ctx:compiladoresParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#for_stmt.
    def enterFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass

    # Exit a parse tree produced by compiladoresParser#for_stmt.
    def exitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expresionl.
    def enterExpresionl(self, ctx:compiladoresParser.ExpresionlContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expresionl.
    def exitExpresionl(self, ctx:compiladoresParser.ExpresionlContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expl.
    def enterExpl(self, ctx:compiladoresParser.ExplContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expl.
    def exitExpl(self, ctx:compiladoresParser.ExplContext):
        pass


    # Enter a parse tree produced by compiladoresParser#terminol.
    def enterTerminol(self, ctx:compiladoresParser.TerminolContext):
        pass

    # Exit a parse tree produced by compiladoresParser#terminol.
    def exitTerminol(self, ctx:compiladoresParser.TerminolContext):
        pass


    # Enter a parse tree produced by compiladoresParser#terml.
    def enterTerml(self, ctx:compiladoresParser.TermlContext):
        pass

    # Exit a parse tree produced by compiladoresParser#terml.
    def exitTerml(self, ctx:compiladoresParser.TermlContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expresion.
    def enterExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expresion.
    def exitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#termino.
    def enterTermino(self, ctx:compiladoresParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#termino.
    def exitTermino(self, ctx:compiladoresParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipeFuncion.
    def enterPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipeFuncion.
    def exitPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#callFuncion.
    def enterCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#callFuncion.
    def exitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#defFuncion.
    def enterDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#defFuncion.
    def exitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argRec.
    def enterArgRec(self, ctx:compiladoresParser.ArgRecContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argRec.
    def exitArgRec(self, ctx:compiladoresParser.ArgRecContext):
        pass


    # Enter a parse tree produced by compiladoresParser#listaArgRec.
    def enterListaArgRec(self, ctx:compiladoresParser.ListaArgRecContext):
        pass

    # Exit a parse tree produced by compiladoresParser#listaArgRec.
    def exitListaArgRec(self, ctx:compiladoresParser.ListaArgRecContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argEnv.
    def enterArgEnv(self, ctx:compiladoresParser.ArgEnvContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argEnv.
    def exitArgEnv(self, ctx:compiladoresParser.ArgEnvContext):
        pass


    # Enter a parse tree produced by compiladoresParser#listaArgEnv.
    def enterListaArgEnv(self, ctx:compiladoresParser.ListaArgEnvContext):
        pass

    # Exit a parse tree produced by compiladoresParser#listaArgEnv.
    def exitListaArgEnv(self, ctx:compiladoresParser.ListaArgEnvContext):
        pass



del compiladoresParser