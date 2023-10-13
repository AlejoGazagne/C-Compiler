# Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#log.
    def visitLog(self, ctx:compiladoresParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retornar.
    def visitRetornar(self, ctx:compiladoresParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#while_stmt.
    def visitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if_stmt.
    def visitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#else_stmt.
    def visitElse_stmt(self, ctx:compiladoresParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#for_stmt.
    def visitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opar.
    def visitOpar(self, ctx:compiladoresParser.OparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oplo.
    def visitOplo(self, ctx:compiladoresParser.OploContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresionLo.
    def visitExpresionLo(self, ctx:compiladoresParser.ExpresionLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expLo.
    def visitExpLo(self, ctx:compiladoresParser.ExpLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#terminoLo.
    def visitTerminoLo(self, ctx:compiladoresParser.TerminoLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termLo.
    def visitTermLo(self, ctx:compiladoresParser.TermLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factorLo.
    def visitFactorLo(self, ctx:compiladoresParser.FactorLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comp.
    def visitComp(self, ctx:compiladoresParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#callFuncion.
    def visitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#defFuncion.
    def visitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        return self.visitChildren(ctx)



del compiladoresParser